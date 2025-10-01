import logging
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from config import Config
from handlers import router  # sizning bot handlers

async def on_startup(bot: Bot):
    await bot.set_webhook(f"{Config.WEBHOOK_URL}{Config.WEBHOOK_PATH}")
    logging.info("Webhook o'rnatildi!")

def main():
    dp = Dispatcher()
    dp.include_router(router)
    dp.startup.register(on_startup)

    bot = Bot(token=Config.API_TOKEN)

    app = web.Application()
    handler = SimpleRequestHandler(dispatcher=dp, bot=bot)
    handler.register(app, path=Config.WEBHOOK_PATH)

    setup_application(app, dp, bot=bot)

    logging.basicConfig(level=logging.INFO)
    web.run_app(app, host="0.0.0.0", port=Config.PORT)

if __name__ == "__main__":
    main()