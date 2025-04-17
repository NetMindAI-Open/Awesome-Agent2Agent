
import fastapi

from router.agent_card_router import agent_card_router
from router.task_router import task_router


api_endpoint_router = fastapi.APIRouter()

api_endpoint_router.include_router(router=agent_card_router)
api_endpoint_router.include_router(router=task_router)
