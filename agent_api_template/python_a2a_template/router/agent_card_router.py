
import fastapi
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from utils.setting_util import setting

agent_card_router = fastapi.APIRouter(prefix="/.well-known")


@agent_card_router.get(
    path="/agent.json"
)
async def get_agent_card(request: Request) -> JSONResponse:
    return JSONResponse(setting.AgentCARD.model_dump(exclude_none=True))
