import logging

from services.chat_control import ChatControlService


async def add_new_chat(event):
    chat_service = ChatControlService()
    chat_id = await chat_service.get_chat_id(event)
    try:
        await chat_service.create(chat_id)
    except Exception as e:
        logging.error(msg=e)

async def delete_chat(event):
    chat_service = ChatControlService()
    chat_id = await chat_service.get_chat_id(event)
    try:
        await chat_service.delete(chat_id)
    except Exception as e:
        logging.error(msg=e)

async def on_message(event):
    chat_service = ChatControlService()
    await chat_service.broadcast_channels(event)

