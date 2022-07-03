from aiogram import Bot, Dispatcher, executor


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
async def echo(message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)   