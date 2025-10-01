from aiogram import Router, types
from aiogram.filters.command import CommandStart

from keyboards.web_app_keyboard import get_webapp_keyboard
from locales import get_message

router = Router(name=__name__)

@router.message(CommandStart())
async def start_handler(message: types.Message):
    lang = message.from_user.language_code
    message_text = get_message('START_MESSAGE', lang)
    await message.answer(
        text=message_text,
        parse_mode="Markdown",
        reply_markup=get_webapp_keyboard()
    )

@router.message()
async def response_every(message: types.Message):
    lang = message.from_user.language_code
    message_text = get_message('UNKNOWN_COMMAND', lang)
    await message.answer(
        text=message_text,
        parse_mode="Markdown",
        reply_markup=get_webapp_keyboard()
    )