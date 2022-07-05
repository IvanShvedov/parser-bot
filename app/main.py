import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from config import Config
from CONSTS import CONFIG_YAML
from storages.postgres import PostgreStorage
from services.chat_control import ChatControlService
from handlers.chat import add_new_chat

config = Config(CONFIG_YAML)

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
dp.register_message_handler(add_new_chat, commands=['add'])

storage = PostgreStorage(
    host = config.DBHOST,
    port = config.DBPORT,
    username = config.DBUSER,
    password = config.DBPASSWORD,
    dbname=config.DBNAME
)
chat_service = ChatControlService(storage=storage, bot=bot)


async def on_startup(dispatcher, url=None, cert=None):
    await storage.connect()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)   