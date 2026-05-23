"""Analytics response shapes — funnel and headline KPIs."""

from __future__ import annotations

from pydantic import BaseModel, Field

from app.models.application import ApplicationStatus


class StageCount(BaseModel):
    stage: ApplicationStatus
    count: int


class FunnelOut(BaseModel):
    """Counts at each pipeline stage + headline conversion rates.

    Active = applications currently sitting at that stage.
    Reached = applications that have ever reached that stage (count + downstream).
    """

    active_by_stage: list[StageCount]
    reached_by_stage: list[StageCount]

    apps_submitted: int = Field(..., description="reached >= applied")
    recruiter_screens: int = Field(..., description="reached >= recruiter_screen")
    tech_screens: int = Field(..., description="reached >= tech_screen")
    onsites: int = Field(..., description="reached >= onsite")
    offers: int = Field(..., description="reached >= offer")
    accepted: int

    app_to_screen_rate: float = Field(..., description="recruiter_screens / apps_submitted")
    screen_to_tech_rate: float
    tech_to_onsite_rate: float
    onsite_to_offer_rate: float
