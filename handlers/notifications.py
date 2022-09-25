import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot

async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id = chat_id, text='ну ок, напомним')

async def if_youresad():
    photo = open('media/lol.jpg', 'rb')
    await bot.send_photo(chat_id=chat_id, photo=photo)
    await bot.send_message(chat_id = chat_id, text="снова понедельник, понимаю...!")

async def scheduler():
    aioschedule.every().monday.at("08:00").do(if_youresad)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)



def register_handlers_notifications(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
    lambda word: "напоминалка" in word.text)

