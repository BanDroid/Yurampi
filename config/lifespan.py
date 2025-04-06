from fastapi import FastAPI
import aiohttp
from contextlib import asynccontextmanager
from config.constant import YURAMANGA_URL
from dependencies.session import SessionsName


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.extra[SessionsName.YuraManga.value] = aiohttp.ClientSession(
        YURAMANGA_URL.geturl()
    )
    yield
    await app.extra[SessionsName.YuraManga.value].close()
