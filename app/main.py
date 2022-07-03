from aiogram import Bot, Dispatcher, executor, types
import asyncio

from config import Config
from CONSTS import CONFIG_YAML
from storages.postgres import PostgreStorage
from services.chat_control import ChatControl


config = Config(CONFIG_YAML)
storage = PostgreStorage(
    host = config.DBHOST,
    port = config.DBPORT,
    username = config.DBUSER,
    password = config.DBPASSWORD,
    dbname=config.DBNAME
)
chat_service = ChatControl(storage=storage)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'hi'])
async def echo(message: types.Message):
    res = await chat_service.create('1111111')
    await bot.copy_message(
        chat_id='-1001544120674',
        from_chat_id = message.chat.id,
        message_id = message.message_id
    )

async def on_startup(dispatcher, url=None, cert=None):
    await storage.connect()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)   