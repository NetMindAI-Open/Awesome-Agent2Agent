
from models.types import (
    SendTaskRequest, 
    SendTaskStreamingRequest,
)
from service.task_manager import InMemoryTaskManager


class CustomTaskManager(InMemoryTaskManager):
    """ TODO
    自定义任务管理器

    custom task manager
    """

    async def on_send_task(self, request: SendTaskRequest):
        pass

    async def on_send_task_subscribe(
        self, request: SendTaskStreamingRequest
    ):
        pass


custom_task_manager = CustomTaskManager()
