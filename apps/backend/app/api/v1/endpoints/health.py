"""Application liveness endpoint."""

from typing import Literal

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.core.config import Settings, get_settings

router = APIRouter(prefix="/health", tags=["health"])


class HealthResponse(BaseModel):
    """Public liveness information for the API process."""

    status: Literal["healthy"]
    service: str
    version: str


@router.get("", response_model=HealthResponse)
def health_check(settings: Settings = Depends(get_settings)) -> HealthResponse:
    """Report that the API process is accepting requests."""
    return HealthResponse(
        status="healthy",
        service=settings.app_name,
        version=settings.app_version,
    )
