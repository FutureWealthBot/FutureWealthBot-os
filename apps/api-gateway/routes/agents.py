from fastapi import APIRouter

router = APIRouter(prefix="/v1/agents", tags=["agents"])


@router.get("/")
async def list_agents() -> dict[str, list[dict[str, str]]]:
    return {"items": []}
