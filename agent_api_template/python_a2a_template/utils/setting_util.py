
import os
import json
from dotenv import load_dotenv

from models.types import AgentCard

load_dotenv()
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_agent_json():
    agent_json_path = os.path.join(BASE_PATH, "static/agent.json")
    with open(agent_json_path, "r", encoding="utf-8") as f:
        agent_json = json.load(f)
    return agent_json


class Setting:
    AgentCARD: AgentCard = AgentCard(**load_agent_json())


setting = Setting()
