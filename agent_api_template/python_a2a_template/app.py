
import asyncio
import click

from utils.setting_util import setting
from service.custom_task_manager import CustomTaskManager
from service.server import A2AServer


@click.command()
@click.option("--host", default="localhost")
@click.option("--port", default=10001)
def main(host, port):

    server = A2AServer(
        host=host,
        port=port,
    )
    server.start()


if __name__ == "__main__":
    main()

