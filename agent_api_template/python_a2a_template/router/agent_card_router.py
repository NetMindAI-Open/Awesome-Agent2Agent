
import fastapi
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from typing import Annotated, Any

from utils.setting_util import setting
from utils.jwt_util import verify_jwt

agent_card_router = fastapi.APIRouter(prefix="/.well-known")


@agent_card_router.get(
    path="/agent.json"
)
async def get_agent_card(
    request: Request,
    _: Annotated[Any, fastapi.Depends(verify_jwt)]
) -> JSONResponse:
    return JSONResponse(setting.AgentCARD.model_dump(exclude_none=True))
