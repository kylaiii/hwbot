from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp



#@dp.callback_query_handler(lambda call: call.data == "button_call1")
async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call1 = InlineKeyboardButton("NEXT", callback_data="button_call2")
    markup.add(button_call1)

    question = 'В каком году вышел фильм "Крестный отец?"'
    answers = [
            '1962',
            '1969',
            '1972',
            '1979',
            '1982'
        ]
    await bot.send_poll(
            chat_id=call.message.chat.id,
            question=question,
            options=answers,
            is_anonymous=False,
            type='quiz',
            correct_option_id=2,
            explanation='Криминальная сага была выпущена в 1972 году',
            open_period=15,
            reply_markup = markup
        )



async def quiz3(call: types.CallbackQuery):
    question = 'Кто написал роман, на котором основана трилогия "Крестный отец"?'
    answers = [
        "Эд Фалько",
        "Марио Пьюзо",
        "Тонино Бенаквиста",
        "Джон Дикки"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Роман написал Марио Пьюзо',
        open_period=15,

    )
def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz2, lambda call: call.data == "button_call1")
    dp.register_callback_query_handler(quiz3, lambda call: call.data == "button_call2")