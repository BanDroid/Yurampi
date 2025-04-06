from fastapi import APIRouter
import routes.yuramanga.router as yuramanga_router

router = APIRouter()
router.include_router(yuramanga_router.router, prefix="/yuramanga", tags=["YuraManga"])
