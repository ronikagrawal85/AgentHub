"""Version 1 API router aggregation."""

from fastapi import APIRouter

from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.readiness import router as readiness_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(readiness_router)
