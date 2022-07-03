from aiogram import types

from services.chat_control import ChatControlService


async def echo(message: types.Message):
    chat_service = ChatControlService()
    res = await chat_service.create('qwer')
    message_id = await bot.copy_message(
        chat_id='-1001544120674',
        from_chat_id = message.chat.id,
        message_id = message.message_id
    )
