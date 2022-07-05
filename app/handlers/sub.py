from aiogram import types

from services.subscription import SubscriptionService


async def create_subscription(message: types.Message):
    sub_service = SubscriptionService()
    a = await sub_service.get_all_subs()
    sub_id = message.from_user.id
    try:
        await sub_service.create(sub=sub_id)
        await sub_service.bot.send_message(
            text=f"Теперь ты подписан на меня",
            chat_id=message.chat.id
        )
    except Exception as e:
        await sub_service.bot.send_message(
            text="Что то пошло не так",
            chat_id=message.chat.id
        )

async def delete_subscription(message: types.Message):
    sub_service = SubscriptionService()
    sub_id = message.from_user.id
    try:
        await sub_service.delete(sub=sub_id)
        await sub_service.bot.send_message(
            text=f"Ты больше не подписан на меня",
            chat_id=message.chat.id
        )
    except Exception as e:
        await sub_service.bot.send_message(
            text="Что то пошло не так",
            chat_id=message.chat.id
        )

async def on_new_message(channel_post: types.Message):
    sub_service = SubscriptionService()
    await sub_service.broadcast(channel_post.text)    