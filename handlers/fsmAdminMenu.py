from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMIN
from database import bot_db


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()
async def fsm_start(message: types.Message):
    if message.from_user.id in ADMIN:
         if message.chat.type == 'private':
             await FSMAdmin.photo.set()
             await message.answer(f'{message.from_user.full_name}, пожалуйста, отправьте фото блюда')
         else:
             await message.answer("пиши в личку")
    else:
        await message.answer('Ты не админ!')

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Как называтся блюдо?")

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Опишите блюдо?")

async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer("Сколько стоит это блюдо?")
async def load_price(message: types.Message, state: FSMContext):
    try:
      if message.text.isdigit():
        async with state.proxy() as data:
          data['price'] = message.text
      await bot.send_photo(message.from_user.id, data['photo'],
                             caption=f"Название блюда: {data['name']}\n"
                                     f"Описание блюда: {data['description']}\n"
                                     f"Цена: {data['price']}\n")
      await bot_db.sql_command_insert(state)
      await state.finish()
      await message.answer("Аппетитно!")
    except:
        await message.answer("Пиши числа!")


def register_handlers_fsmAdminMenu(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['go'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
