import logging

from services.chat_control import ChatControlService


async def add_new_chat(event):
    chat_service = ChatControlService()
    chat_id = await chat_service.get_chat_id(event)
    try:
        await chat_service.create(chat_id)
        e = await chat_service.client.get_entity('me')
        await chat_service.client.send_message(entity=e, message=f'ID:{chat_id} успешно добавлен в базу')
    except Exception as e:
        logging.error(msg=e)

async def delete_chat(event):
    chat_service = ChatControlService()
    chat_id = await chat_service.get_chat_id(event)
    try:
        await chat_service.delete(chat_id)
        e = await chat_service.client.get_entity('me')
        await chat_service.client.send_message(entity=e, message=f'ID:{chat_id} успешно удален из базы')
    except Exception as e:
        logging.error(msg=e)


async def on_message(event):
    chat_service = ChatControlService()
    channels = await chat_service.get_all()
    for chan in channels:
        e = await chat_service.client.get_entity(int(chan.channel))
        await chat_service.client.send_message(entity=e, message=event.message.message)
