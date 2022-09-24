from aiogram import types, Dispatcher
from config import bot, dp, ADMIN


async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMIN:
            await message.reply("Ты не мой босс!!!")
        elif not message.reply_to_message:
            await message.reply("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(message.chat.id,
                                       message.reply_to_message.from_user.id)
            await message.answer(f"{message.from_user.first_name} братан "
                                 f"кикнул пользователя "
                                 f"{message.reply_to_message.from_user.full_name}")
    else:
        await message.reply("Пиши в группе!")


def register_handlers_admin(dp: Dispatcher):


    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')