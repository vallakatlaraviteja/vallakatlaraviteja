"""State machine unit tests — pure Python, no DB.

These guard the rules in services/application_service.py so a refactor
or stray edit can't silently let an application skip stages.
"""

from __future__ import annotations

import pytest

from app.models.application import ApplicationStatus
from app.services.application_service import valid_transition

S = ApplicationStatus

LEGAL_FORWARD: list[tuple[ApplicationStatus, ApplicationStatus]] = [
    (S.saved, S.tailoring),
    (S.saved, S.ready_to_apply),
    (S.saved, S.applied),
    (S.tailoring, S.ready_to_apply),
    (S.tailoring, S.applied),
    (S.ready_to_apply, S.applied),
    (S.applied, S.recruiter_screen),
    (S.recruiter_screen, S.tech_screen),
    (S.tech_screen, S.onsite),
    (S.onsite, S.offer),
    (S.offer, S.accepted),
]

ILLEGAL_FORWARD: list[tuple[ApplicationStatus, ApplicationStatus]] = [
    (S.saved, S.recruiter_screen),     # skip applied
    (S.saved, S.offer),                # skip many
    (S.applied, S.tech_screen),        # skip recruiter_screen
    (S.recruiter_screen, S.onsite),    # skip tech_screen
    (S.tech_screen, S.offer),          # skip onsite
    (S.accepted, S.applied),           # backward
    (S.rejected, S.applied),           # terminal
    (S.withdrawn, S.applied),          # terminal
]


@pytest.mark.parametrize(("src", "dst"), LEGAL_FORWARD)
def test_legal_forward_transitions(src: ApplicationStatus, dst: ApplicationStatus) -> None:
    assert valid_transition(src, dst) is True


@pytest.mark.parametrize(("src", "dst"), ILLEGAL_FORWARD)
def test_illegal_forward_transitions(src: ApplicationStatus, dst: ApplicationStatus) -> None:
    assert valid_transition(src, dst) is False


@pytest.mark.parametrize(
    "active",
    [S.saved, S.tailoring, S.ready_to_apply, S.applied, S.recruiter_screen, S.tech_screen, S.onsite, S.offer],
)
def test_can_reject_or_withdraw_from_any_active_stage(active: ApplicationStatus) -> None:
    assert valid_transition(active, S.rejected) is True
    assert valid_transition(active, S.withdrawn) is True


def test_self_transition_is_idempotent() -> None:
    for s in ApplicationStatus:
        assert valid_transition(s, s) is True
