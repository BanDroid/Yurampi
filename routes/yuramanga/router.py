from fastapi import APIRouter
from .controller import get_manga, get_mangas

router = APIRouter()
router.get("/manga")(get_mangas)
router.get("/manga/{slug}")(get_manga)
