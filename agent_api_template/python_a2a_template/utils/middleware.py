
import json
from typing import AsyncIterable, Any
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint, _StreamingResponse
from sse_starlette.sse import EventSourceResponse

from models.types import (
    JSONRPCResponse,
    InvalidRequestError,
    JSONParseError,
    InternalError,
)
from utils.logging_util import logger
from utils.setting_util import setting


def _handle_exception(e: Exception) -> JSONResponse:
    if isinstance(e, json.decoder.JSONDecodeError):
        json_rpc_error = JSONParseError()
    elif isinstance(e, ValidationError):
        json_rpc_error = InvalidRequestError(data=json.loads(e.json()))
    else:
        logger.error(f"Unhandled exception: {e}")
        json_rpc_error = InternalError()

    response = JSONRPCResponse(id=None, error=json_rpc_error)
    return JSONResponse(response.model_dump(exclude_none=True), status_code=400)


def _create_response(result: Any) -> JSONResponse | EventSourceResponse:
    if isinstance(result, AsyncIterable):

        async def event_generator(result) -> AsyncIterable[dict[str, str]]:
            async for item in result:
                yield {"data": item.model_dump_json(exclude_none=True)}

        return EventSourceResponse(event_generator(result))
    elif isinstance(result, JSONRPCResponse):
        return JSONResponse(result.model_dump(exclude_none=True))
    elif isinstance(result, _StreamingResponse):
        return result
    else:
        logger.error(f"Unexpected result type: {type(result)}")
        raise ValueError(f"Unexpected result type: {type(result)}")


class CustomMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        # Pre-processing logic
        if setting.AgentCARD.authentication:
            await self.request_auth(request)

        try:
            result = await call_next(request)
            return _create_response(result)
        except Exception as e:
            return _handle_exception(e)
        # Post-processing logic

    async def request_auth(self, request: Request):
        # Implement your authentication logic here
        pass
