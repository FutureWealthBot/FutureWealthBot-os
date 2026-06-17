from fastapi import FastAPI

from .routes.agents import router as agents_router
from .routes.health import router as health_router


def create_app() -> FastAPI:
    app = FastAPI(title="FUTUREWEALTHBOT OS API Gateway", version="0.1.0")
    app.include_router(health_router)
    app.include_router(agents_router)
    return app


app = create_app()
