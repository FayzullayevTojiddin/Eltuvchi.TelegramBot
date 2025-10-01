# locales/__init__.py
import importlib

AVAILABLE_LANGUAGES = ['uz', 'ru', 'en']
DEFAULT_LANGUAGE = 'uz'


def get_message(key: str, lang: str = None):
    lang_code = lang or DEFAULT_LANGUAGE
    if lang_code not in AVAILABLE_LANGUAGES:
        raise ValueError(f"Language '{lang_code}' not supported.")

    module = importlib.import_module(f".{lang_code}", package=__name__)

    return getattr(module, key, key)