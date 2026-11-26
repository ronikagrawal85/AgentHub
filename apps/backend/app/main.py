from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import Settings, get_settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import configure_structured_logging
from app.core.middleware import CorrelationIdMiddleware, ExceptionBoundaryMiddleware


def create_app(settings: Settings | None = None) -> FastAPI:
    """Create and configure an AgentHub API application instance."""
    app_settings = settings or get_settings()
    configure_structured_logging(app_settings.log_level)
    application = FastAPI(
        title=app_settings.app_name,
        version=app_settings.app_version,
        debug=app_settings.debug,
    )
    register_exception_handlers(application)
    application.add_middleware(ExceptionBoundaryMiddleware)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=app_settings.cors_allowed_origins,
        allow_credentials=app_settings.cors_allow_credentials,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.add_middleware(CorrelationIdMiddleware)
    application.include_router(api_router, prefix=app_settings.api_v1_prefix)

    if settings is not None:
        application.dependency_overrides[get_settings] = lambda: app_settings

    return application


app = create_app()
