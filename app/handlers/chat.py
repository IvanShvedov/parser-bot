from aiogram import types

from services.chat_control import ChatControlService


async def add_new_chat(message: types.Message):
    chat_service = ChatControlService()
    chat_id = message.get_args()
    if chat_id is None or chat_id == "":
        await chat_service.bot.send_message(
            text="Отправь мне id чата через команду /add и я добавлю его в базу\n - /add 12345678910",
            chat_id=message.chat.id    
        )
        return
    try:
        await chat_service.create(chat_id)
        await chat_service.bot.send_message(
            text=f"{chat_id} успешно добавлен",
            chat_id=message.chat.id
        )
    except Exception as e:
        await chat_service.bot.send_message(
            text="Что то пошло не так",
            chat_id=message.chat.id
        )

async def delete_chat(message: types.Message):
    chat_service = ChatControlService()
    chat_id = message.get_args()
    if chat_id is None or chat_id == "":
        await chat_service.bot.send_message(
            text="Отправь мне id чата через команду /del и я удалю его из базы\n - /del 12345678910",
            chat_id=message.chat.id    
        )
        return
    try:
        await chat_service.delete(chat_id)
        await chat_service.bot.send_message(
            text=f"{chat_id} успешно удален",
            chat_id=message.chat.id
        )
    except Exception as e:
        await chat_service.bot.send_message(
            text="Что то пошло не так",
            chat_id=message.chat.id
        )

# async def on_new_message(message: types.Message):
#     chat_service = ChatControlService()
#     await chat_service.bot.copy_message(
#         chat_id=''
#         from_chat_id=message.chat.id,
#         message_id = message.message_id
#     )
