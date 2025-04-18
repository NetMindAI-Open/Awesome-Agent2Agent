
import fastapi
from fastapi.requests import Request
from typing import Annotated, Any

from models.types import (
    A2ARequest,
    GetTaskRequest,
    SendTaskRequest,
    SendTaskStreamingRequest,
    CancelTaskRequest,
    SetTaskPushNotificationRequest,
    GetTaskPushNotificationRequest,
    TaskResubscriptionRequest,
)
from utils.logging_util import logger
from utils.jwt_util import verify_jwt
from service.custom_task_manager import custom_task_manager


task_router = fastapi.APIRouter(prefix="/tasks")


async def _process_request(request: Request):
    body = await request.json()
    json_rpc_request = A2ARequest.validate_python(body)

    if isinstance(json_rpc_request, GetTaskRequest):
        result = await custom_task_manager.on_get_task(json_rpc_request)
    elif isinstance(json_rpc_request, SendTaskRequest):
        result = await custom_task_manager.on_send_task(json_rpc_request)
    elif isinstance(json_rpc_request, SendTaskStreamingRequest):
        result = await custom_task_manager.on_send_task_subscribe(
            json_rpc_request
        )
    elif isinstance(json_rpc_request, CancelTaskRequest):
        result = await custom_task_manager.on_cancel_task(json_rpc_request)
    elif isinstance(json_rpc_request, SetTaskPushNotificationRequest):
        result = await custom_task_manager.on_set_task_push_notification(json_rpc_request)
    elif isinstance(json_rpc_request, GetTaskPushNotificationRequest):
        result = await custom_task_manager.on_get_task_push_notification(json_rpc_request)
    elif isinstance(json_rpc_request, TaskResubscriptionRequest):
        result = await custom_task_manager.on_resubscribe_to_task(
            json_rpc_request
        )
    else:
        logger.warning(f"Unexpected request type: {type(json_rpc_request)}")
        raise ValueError(f"Unexpected request type: {type(request)}")

    return result


@task_router.post(
    path="/get"
)
async def get_task(
    request: Request,
    _: Annotated[Any, fastapi.Depends(verify_jwt)],
) -> fastapi.Response:
    result = await _process_request(request)
    return result


@task_router.post(
    path="/send"
)
async def send_task(
    request: Request,
    _: Annotated[Any, fastapi.Depends(verify_jwt)],
) -> fastapi.Response:
    result = await _process_request(request)
    return result


@task_router.post(
    path="/sendSubscribe"
)
async def send_task_subscribe(
    request: Request,
    _: Annotated[Any, fastapi.Depends(verify_jwt)],
) -> fastapi.Response:
    result = await _process_request(request)
    return result


@task_router.post(
    path="/cancel"
)
async def cancel_task(
    request: Request,
    _: Annotated[Any, fastapi.Depends(verify_jwt)],
) -> fastapi.Response:
    result = await _process_request(request)
    return result


@task_router.post(
    path="/pushNotification/set"
)
async def set_task_push_notification(
    request: Request,
    _: Annotated[Any, fastapi.Depends(verify_jwt)],
) -> fastapi.Response:
    result = await _process_request(request)
    return result


@task_router.post(
    path="/pushNotification/get"
)
async def get_task_push_notification(
    request: Request,
    _: Annotated[Any, fastapi.Depends(verify_jwt)],
) -> fastapi.Response:
    result = await _process_request(request)
    return result


@task_router.post(
    path="/resubscribe"
)
async def resubscribe_to_task(
    request: Request,
    _: Annotated[Any, fastapi.Depends(verify_jwt)],
) -> fastapi.Response:
    result = await _process_request(request)
    return result
