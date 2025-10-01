from aiogram import Bot, Dispatcher
from aiohttp import web
from config import Config
from handlers import router
import asyncio
import logging

WEBHOOK_URL = f"{Config.WEBHOOK_URL}{Config.WEBHOOK_PATH}"

async def on_startup(bot: Bot):
    await bot.delete_webhook()
    await bot.set_webhook(WEBHOOK_URL)
    logging.info("Webhook Set!")

async def handle(request: web.Request):
    update = await request.json()
    await request.app['dp'].process_update(update)
    return web.Response()

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=Config.API_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    app = web.Application()
    app['dp'] = dp
    app.router.add_post(Config.WEBHOOK_PATH, handle)
    await on_startup(bot)
    web.run_app(app, host="0.0.0.0", port=Config.PORT)

if __name__ == "__main__":
    asyncio.run(main())