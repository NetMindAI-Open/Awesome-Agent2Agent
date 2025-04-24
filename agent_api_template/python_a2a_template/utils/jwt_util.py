
import time
from jose import jwt as jose_jwt
from jose.exceptions import ExpiredSignatureError, JWTError
from typing import Annotated, Any
from collections.abc import AsyncGenerator
from fastapi import Depends, Header, HTTPException

import sys
sys.path.append('/root/liss_package/Awesome-Agent2Agent/agent_api_template/python_a2a_template')
from utils.setting_util import setting


def create_jwt_token() -> str:
    data = {
        "current_time": int(time.time()),
    }
    token = jose_jwt.encode(
        data,
        setting.APISecretKey,
        algorithm="HS256",
    )
    return token


def decode_jwt_token(token: str) -> dict:
    data = jose_jwt.decode(
        token,
        setting.APISecretKey,
        algorithms=["HS256"],
    )
    return data


async def extract_token(token: str | None = Header(default=None)) -> AsyncGenerator[str, Any]:
    if not setting.AgentCARD.authentication:
        yield None
        return

    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized, token is required")

    if not token.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Login status is abnormal. Please log in again before proceeding.")

    token = token.split(" ")[1]
    yield token


async def verify_jwt(
    token: Annotated[str, Depends(extract_token)],
) -> AsyncGenerator[Any]:
    if not setting.AgentCARD.authentication:
        yield None
        return
    try:
        data = decode_jwt_token(token)
        yield data
    except JWTError as e:
        raise HTTPException(status_code=401, detail="Invalid token") from e
