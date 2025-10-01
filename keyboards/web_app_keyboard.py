from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

def get_webapp_keyboard(url: str = "https://eltuvchi.uz", text: str = "Eltuvchi Web") -> InlineKeyboardMarkup:
    web_app_button = InlineKeyboardButton(
        text=text,
        web_app=WebAppInfo(url=url)
    )
    return InlineKeyboardMarkup(inline_keyboard=[[web_app_button]])