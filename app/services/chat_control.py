from telethon import TelegramClient
import re

from storages.base_storage import Storage
from models.channel import ChannelDTO
from .queries import INSERT_INTO_CHANNELS, DELETE_FROM_CHANNELS, SELECT_ALL_FROM_CHANNELS


class ChatControlService:

    def __new__(cls, storage: Storage = None, client: TelegramClient = None):
        if not hasattr(cls, '_instance'):
            cls.storage = storage
            cls.client = client
            cls._instance = super().__new__(cls)
        return cls._instance

    async def create(self, chat_id: str):
        res = await self.storage.create(INSERT_INTO_CHANNELS.format(chat_id=chat_id))
        e = await self.client.get_entity('me')
        await self.client.send_message(entity=e, message=f'ID:{chat_id} успешно добавлен в базу')
        return res

    async def delete(self, chat_id: str):
        res = await self.storage.delete(DELETE_FROM_CHANNELS.format(chat_id=chat_id))
        e = await self.client.get_entity('me')
        await self.client.send_message(entity=e, message=f'ID:{chat_id} успешно удален из базы')
        return res

    async def get_all(self):
        res = await self.storage.get_all(SELECT_ALL_FROM_CHANNELS)
        channels = await self._parse(res)
        return channels

    async def get_chat_id(self, event):
        chat_id = re.sub(
            r'/del ', '', re.sub(
                r'/add ', '', event.raw_text
            )
        )
        return chat_id

    async def broadcast_channels(self, event):
        channels = await self.get_all()
        for chan in channels:
            e = await self.client.get_entity(int(chan.channel))
            await self.client.send_message(entity=e, message=event.message.message)

    async def _parse(self, body):
        channels = []
        for item in body:
            channel = ChannelDTO()
            for key in item:
                setattr(channel, key, item[key])
            channels.append(channel)
        return channels