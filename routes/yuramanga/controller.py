import aiohttp
from fastapi import Depends, HTTPException
from dependencies.session import SessionsName, get_session
from .schemas import Manga, MangasResponse
from .parser import parse_mangas_from_html_str, parse_manga_from_html_str


async def get_mangas(
    page: int = 1,
    session: aiohttp.ClientSession = Depends(get_session(SessionsName.YuraManga.value)),
) -> MangasResponse:
    async with session.get(f"/page/{page}") as res:
        if not res.ok or res.status != 200:
            return MangasResponse(
                ok=False,
                page=page,
                totalPages=0,
                items=[],
            )
        parsed_items = await parse_mangas_from_html_str(await res.text())
        if not parsed_items:
            return MangasResponse(
                ok=False,
                page=page,
                totalPages=0,
                items=[],
            )
        return MangasResponse(
            ok=True,
            page=page,
            totalPages=0,
            items=parsed_items,
        )


async def get_manga(
    slug: str = "",
    session: aiohttp.ClientSession = Depends(get_session(SessionsName.YuraManga.value)),
) -> Manga:
    async with session.get(f"/series/{slug}") as res:
        if not res.ok or res.status != 200:
            raise HTTPException(status_code=res.status, detail=res.reason)
        parsed_item = await parse_manga_from_html_str(await res.text())
        return parsed_item
