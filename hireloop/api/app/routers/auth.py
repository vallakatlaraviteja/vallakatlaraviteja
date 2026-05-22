"""Single-owner auth: dev login that issues a session for the configured OWNER_EMAIL.

In production this can be swapped for magic-link email auth without changing
any other module — see core/security.py.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import BaseModel, EmailStr

from app.config import Settings, get_settings
from app.core.security import issue_session, require_owner, revoke_session

router = APIRouter()


class LoginRequest(BaseModel):
    email: EmailStr


class WhoAmI(BaseModel):
    email: EmailStr


@router.post("/login", summary="Issue a session for the configured owner email")
async def login(
    body: LoginRequest,
    response: Response,
    settings: Settings = Depends(get_settings),
) -> WhoAmI:
    if body.email.lower() != settings.owner_email.lower():
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not the owner")
    issue_session(response, settings.owner_email)
    return WhoAmI(email=settings.owner_email)


@router.post("/logout")
async def logout(response: Response) -> dict[str, str]:
    revoke_session(response)
    return {"status": "ok"}


@router.get("/me", summary="Current owner identity")
async def me(email: str = Depends(require_owner)) -> WhoAmI:
    return WhoAmI(email=email)
