import asyncio
import logging
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from config import Config
from handlers import router

async def handle(request: web.Request):
    data = await request.json()
    update = Update(**data)
    dp: Dispatcher = request.app['dp']
    dp.feed_update(update)  # Aiogram 3.x da synchronous, await kerak emas
    return web.Response()

async def on_startup(app: web.Application):
    bot: Bot = app['bot']
    await bot.delete_webhook()
    await bot.set_webhook(f"{Config.WEBHOOK_URL}{Config.WEBHOOK_PATH}")
    logging.info("Webhook set!")

async def create_app():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=Config.API_TOKEN)
    dp = Dispatcher(bot=bot)
    dp.include_router(router)

    app = web.Application()
    app['bot'] = bot
    app['dp'] = dp
    app.router.add_post(Config.WEBHOOK_PATH, handle)
    app.on_startup.append(on_startup)

    return app

if __name__ == "__main__":
    app = asyncio.run(create_app())
    web.run_app(app, host="0.0.0.0", port=Config.PORT)
