# from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel


class Genre(BaseModel):
    name: str


class Chapter(BaseModel):
    chapter_url: str
    name: str
    updated_at: Optional[str]


class Manga(BaseModel):
    series_url: str
    title: str
    alternative_title: Optional[str] = None
    type: str
    cover_uri: Optional[str] = ""
    genres: Optional[list[Genre]] = []
    chapters: Optional[list[Chapter]] = []
    latest_chapters: Optional[list[Chapter]] = None


class MangasResponse(BaseModel):
    ok: bool
    page: int
    totalPages: int
    items: list[Manga]
