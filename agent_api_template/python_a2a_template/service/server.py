
import fastapi
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from utils.logging_util import logger
from utils.setting_util import setting
from utils.middleware import CustomMiddleware
from router import api_endpoint_router
from service.task_manager import TaskManager


class A2AServer:
    def __init__(
        self,
        host="0.0.0.0",
        port=5000,
        endpoint="/",
    ):
        self.host = host
        self.port = port
        self.endpoint = endpoint
        self.app = fastapi.FastAPI(default_response_class=ORJSONResponse)
        self.app.add_middleware(CustomMiddleware)
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        self.app.include_router(router=api_endpoint_router)

    def start(self):
        import uvicorn

        uvicorn.run(self.app, host=self.host, port=self.port)
