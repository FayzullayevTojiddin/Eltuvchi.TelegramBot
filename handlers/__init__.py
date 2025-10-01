from aiogram import Router
from .main_handler import router as main_handler_router

router = Router(name=__name__)

router.include_routers(main_handler_router)