from enum import Enum
from fastapi import Request


class SessionsName(Enum):
    YuraManga = "session_yuramanga"


def get_session(name: str):
    def session(request: Request):
        if not name.startswith("session_"):
            return request.app.extra[f"session_{name}"]
        return request.app.extra[name]

    return session
