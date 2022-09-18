from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp



#@dp.message_handler(commands=['quiz'])
async def quiz(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call1 = InlineKeyboardButton("NEXT",  callback_data="button_call1")
    markup.add(button_call1)

    question = "Как звали младшего сына Дона Корлеоне?"
    answers = [
        'Сантино',
        'Фредерико',
        'Антонио',
        'Майкл',
        'Том',
        'Паоло'
    ]
    await bot.send_poll(
        chat_id= message.chat.id,
        question = question,
        options = answers,
        is_anonymous=False,
        type = 'quiz',
        correct_option_id=3,
        explanation='Майкл Корлеоне - младший сын Дона',
        open_period = 15,
        reply_markup=markup)


#@dp.message_handler(commands=["mem"])
async def command_start(message: types.Message):
    photo = open('media/013e78fb-7c3f-4ad3-9387-8a69ee9695de.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo)

async def pin(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команда должна быть ответом на сообщение!")
    else:
        await bot.pin_chat_message(message.chat.id,
                                message.reply_to_message.message_id)




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_message_handler(command_start, commands=["mem"])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')

