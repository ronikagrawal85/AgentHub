from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import Settings, get_settings
from app.core.exceptions import register_exception_handlers


def create_app(settings: Settings | None = None) -> FastAPI:
    """Create and configure an AgentHub API application instance."""
    app_settings = settings or get_settings()
    application = FastAPI(
        title=app_settings.app_name,
        version=app_settings.app_version,
        debug=app_settings.debug,
    )
    register_exception_handlers(application)
    application.include_router(api_router, prefix=app_settings.api_v1_prefix)

    if settings is not None:
        application.dependency_overrides[get_settings] = lambda: app_settings

    return application


app = create_app()
