"""Analytics router — funnel KPIs computed from applications + events.

The funnel answers: for each pipeline stage, how many of my applications
ever reached this stage? Conversion rates fall out as ratios of consecutive
stage counts.

We compute "reached" by taking the union of two signals per application:
  1. its current status (if in the funnel order)
  2. every `to` stage from its append-only event history

The max stage in that union is the deepest stage the application reached;
it counts toward that stage and every shallower stage.
"""

from __future__ import annotations

import uuid
from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import require_owner
from app.db import get_session
from app.models.application import Application, ApplicationStatus
from app.models.event import Event, EventKind
from app.schemas.analytics import FunnelOut, StageCount
from app.services.candidate_service import get_or_create_owner

router = APIRouter()

_STAGE_ORDER: list[ApplicationStatus] = [
    ApplicationStatus.applied,
    ApplicationStatus.recruiter_screen,
    ApplicationStatus.tech_screen,
    ApplicationStatus.onsite,
    ApplicationStatus.offer,
    ApplicationStatus.accepted,
]
_STAGE_INDEX: dict[ApplicationStatus, int] = {s: i for i, s in enumerate(_STAGE_ORDER)}


def _safe_div(num: int, den: int) -> float:
    return round((num / den), 4) if den else 0.0



@router.get("/funnel", response_model=FunnelOut, summary="Pipeline funnel + conversion rates")
async def funnel(
    _: str = Depends(require_owner),
    session: AsyncSession = Depends(get_session),
) -> FunnelOut:
    owner = await get_or_create_owner(session)

    # Active = current status grouping. All statuses appear, including saved /
    # tailoring / ready_to_apply / rejected / withdrawn.
    active_q = (
        select(Application.status, func.count(Application.id))
        .where(Application.candidate_id == owner.id)
        .group_by(Application.status)
    )
    active_map: dict[ApplicationStatus, int] = {
        s: c for s, c in (await session.execute(active_q)).all()
    }

    # Per-application max stage reached. Seed from current status, then merge
    # in every `to` from the status-change event log.
    max_stage_idx: dict[uuid.UUID, int] = {}

    cur_q = select(Application.id, Application.status).where(
        Application.candidate_id == owner.id
    )
    for app_id, current in (await session.execute(cur_q)).all():
        if current in _STAGE_INDEX:
            max_stage_idx[app_id] = _STAGE_INDEX[current]

    ev_q = select(Event.application_id, Event.payload).where(
        Event.candidate_id == owner.id,
        Event.kind == EventKind.application_status_changed,
        Event.application_id.is_not(None),
    )
    for app_id, payload in (await session.execute(ev_q)).all():
        if not isinstance(payload, dict):
            continue
        target = payload.get("to")
        try:
            stage = ApplicationStatus(target) if target else None
        except ValueError:
            stage = None
        if stage in _STAGE_INDEX:
            idx = _STAGE_INDEX[stage]
            prev = max_stage_idx.get(app_id, -1)
            if idx > prev:
                max_stage_idx[app_id] = idx

    # Tally: each app counts toward its max stage AND every shallower stage.
    reached_counts: dict[ApplicationStatus, int] = {s: 0 for s in _STAGE_ORDER}
    for idx in max_stage_idx.values():
        for shallower in _STAGE_ORDER[: idx + 1]:
            reached_counts[shallower] += 1



    apps_submitted = reached_counts[ApplicationStatus.applied]
    recruiter_screens = reached_counts[ApplicationStatus.recruiter_screen]
    tech_screens = reached_counts[ApplicationStatus.tech_screen]
    onsites = reached_counts[ApplicationStatus.onsite]
    offers = reached_counts[ApplicationStatus.offer]
    accepted = reached_counts[ApplicationStatus.accepted]

    return FunnelOut(
        active_by_stage=[
            StageCount(stage=s, count=active_map.get(s, 0)) for s in ApplicationStatus
        ],
        reached_by_stage=[
            StageCount(stage=s, count=reached_counts[s]) for s in _STAGE_ORDER
        ],
        apps_submitted=apps_submitted,
        recruiter_screens=recruiter_screens,
        tech_screens=tech_screens,
        onsites=onsites,
        offers=offers,
        accepted=accepted,
        app_to_screen_rate=_safe_div(recruiter_screens, apps_submitted),
        screen_to_tech_rate=_safe_div(tech_screens, recruiter_screens),
        tech_to_onsite_rate=_safe_div(onsites, tech_screens),
        onsite_to_offer_rate=_safe_div(offers, onsites),
    )
