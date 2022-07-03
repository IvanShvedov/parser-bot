from aiogram import Bot, Dispatcher, executor

from config import Config
from CONSTS import CONFIG_YAML
from storages.postgres import PostgreStorage
from services.chat_control import ChatControlService
from handlers.chat import echo

config = Config(CONFIG_YAML)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)
dp.register_message_handler(echo, commands=['hi'])

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