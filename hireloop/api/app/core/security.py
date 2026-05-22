"""Single-owner cookie session. Multi-tenant migration is a swap of this module."""

from __future__ import annotations

from fastapi import Cookie, Depends, HTTPException, Response, status
from itsdangerous import BadSignature, URLSafeSerializer

from app.config import Settings, get_settings

SESSION_COOKIE = "hireloop_session"
SESSION_MAX_AGE = 60 * 60 * 24 * 30  # 30 days


def _serializer(settings: Settings) -> URLSafeSerializer:
    return URLSafeSerializer(settings.session_secret, salt="hireloop-session")


def issue_session(response: Response, email: str) -> None:
    settings = get_settings()
    token = _serializer(settings).dumps({"email": email})
    response.set_cookie(
        key=SESSION_COOKIE,
        value=token,
        max_age=SESSION_MAX_AGE,
        httponly=True,
        samesite="lax",
        secure=settings.environment != "local",
    )


def revoke_session(response: Response) -> None:
    response.delete_cookie(SESSION_COOKIE)


def require_owner(
    hireloop_session: str | None = Cookie(default=None),
    settings: Settings = Depends(get_settings),
) -> str:
    """Return the owner email, or 401. Single-owner enforcement."""
    if not hireloop_session:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    try:
        payload = _serializer(settings).loads(hireloop_session)
    except BadSignature as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid session"
        ) from exc
    email = str(payload.get("email", ""))
    if email.lower() != settings.owner_email.lower():
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not the owner")
    return email
