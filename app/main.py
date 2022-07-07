import logging
import asyncio

from telethon import events, TelegramClient

from config import Config
from CONSTS import CONFIG_YAML
from storages.postgres import PostgreStorage
from services.chat_control import ChatControlService
from handlers.chat import add_new_chat, delete_chat, on_message

config = Config(CONFIG_YAML)


logging.basicConfig(level=logging.INFO)

client = TelegramClient('test', config.API_ID, config.API_HASH)

client.add_event_handler(on_message, events.NewMessage)

storage = PostgreStorage(
    host = config.DBHOST,
    port = config.DBPORT,
    username = config.DBUSER,
    password = config.DBPASSWORD,
    dbname=config.DBNAME
)
chat_service = ChatControlService(storage=storage, client=client)


if __name__ == '__main__':
    client.start()
    client.loop.create_task(storage.connect())
    client.run_until_disconnected()

