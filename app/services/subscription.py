from aiogram import Bot

from storages.base_storage import Storage
from .queries import INSERT_INTO_SUBS, DELETE_FROM_SUBS, SELECT_ALL_FROM_SUBS
from models.sub import SubDTO


class SubscriptionService:

    def __new__(cls, storage: Storage = None, bot: Bot = None):
        if not hasattr(cls, '_instance'):
            cls.storage = storage
            cls.bot = bot
            cls._instance = super().__new__(cls)
        return cls._instance

    async def get_all_subs(self):
        res = await self.storage.get_all(SELECT_ALL_FROM_SUBS)
        subs = await self._parse_body(res)
        return subs

    async def create(self, sub: str):
        res = await self.storage.create(INSERT_INTO_SUBS.format(sub=sub))
        return res

    async def delete(self, sub: str):
        res = await self.storage.delete(DELETE_FROM_SUBS.format(sub=sub))
        return res

    async def broadcast(self, message):
        subs = await self.get_all_subs()
        for sub in subs:
            await self.bot.send_message(chat_id=sub.sub, text=message)
            

    async def _parse_body(self, body):
        subs = []
        try:
            for item in body:
                sub = SubDTO()
                for key in item:
                    setattr(sub, key, item[key])
                subs.append(sub)
        except TypeError:
            pass
        return subs