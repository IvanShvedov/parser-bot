from aiogram import Bot

from storages.base_storage import Storage


class ChatControlService:

    def __new__(cls, storage: Storage = None, bot: Bot = None):
        if not hasattr(cls, '_instance'):
            cls.storage = storage
            cls.bot = bot
            cls._instance = super().__new__(cls)
        return cls._instance

    async def create(self, chat_id: str):
        res = await self.storage.create(f"insert into channels (channel) values ('{chat_id}')")
        return res

    async def delete(self, chat_id: str):
        res = await self.storage.delete(f"delete from channels where channels.channel={chat_id}")
        return res