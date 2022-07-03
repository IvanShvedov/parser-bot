from aiogram import Bot, Dispatcher, executor, types


from config import Config
from CONSTS import CONFIG_YAML
from storages.postgres import PostgreStorage


config = Config(CONFIG_YAML)
storage = PostgreStorage(
    host = config.DBHOST,
    port = config.DBPORT,
    username = config.DBUSER,
    password = config.DBPASSWORD,
    dbname=config.DBNAME
)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'hi'])
async def echo(message: types.Message):
    await bot.copy_message(chat_id='-1001544120674', from_chat_id = message.chat.id, message_id = message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)   