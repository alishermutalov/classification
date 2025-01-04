from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
#internal packages
from loader import bot, dp
from keyboards.inline import education_btn
from utils.states import Human
from config import TELEGRAM_GROUP_ID
from utils.formatting import group_formatter
from data.google_sheets import save_to_gsheet
from utils.id_generator import get_next_unique_number

@dp.callback_query(StateFilter(Human.gender), F.data.startswith("gender:"))
async def selected_gender(call:CallbackQuery, state:FSMContext):
    gender = call.data.split(":")[1]
    await state.update_data(gender=gender)
    await call.message.edit_text(f"You selected: {gender}")
    await state.set_state(Human.age)
    await bot.send_message(chat_id=call.from_user.id, text="How old is the person? (Enter a number in years)")
    
@dp.message(Human.age)
async def get_age(message:Message, state:FSMContext):
    try:
        if int(message.text)>0:
            await state.update_data(age=int(message.text))
            await state.set_state(Human.nationality)
            await message.answer("What is their nationality? (e.g., American, French)")
        else:
            await message.answer("Age must be only positive numbers!")
    except:
        await message.answer("Age must be only positive numbers!")
    
@dp.message(Human.nationality)
async def get_nationality(message:Message, state:FSMContext):
    await state.update_data(nationality = message.text)
    await state.set_state(Human.education)
    await message.answer("What is their level of education?", reply_markup=education_btn)
    
@dp.callback_query(Human.education)
async def get_education_level(call:CallbackQuery, state:FSMContext):
    education = call.data.split(":")[1]
    await state.update_data(education=education)
    await call.message.edit_text(f"You selected: {education}")
    await state.set_state(Human.eye_color)
    await bot.send_message(chat_id=call.from_user.id, 
                           text="What is their eye color?")
    
@dp.message(Human.eye_color)
async def get_eye_color(message:Message, state:FSMContext):
    await state.update_data(eye_color=message.text)
    await state.set_state(Human.hair_color)
    await message.answer("What is their hair color?")
    
@dp.message(Human.hair_color)
async def get_hair_color(message:Message, state:FSMContext):
    await state.update_data(hair_color=message.text)
    await state.set_state(Human.height)
    await message.answer("What is their height in cm? (Enter a number in cm)")
    
@dp.message(Human.height)
async def get_height(message:Message, state:FSMContext):
    try:
        if int(message.text)>0:
            await state.update_data(height=int(message.text))
            await state.update_data(type='Human')
            await state.update_data(id=f"#{get_next_unique_number()}")
            data = await state.get_data()
            await bot.send_message(chat_id=TELEGRAM_GROUP_ID, text=group_formatter(data, message.from_user.full_name))
            save_to_gsheet(data,message.from_user.full_name)
            await message.answer("All data saved!")
            await state.clear()
        else:
            await message.answer("Height must be positive numbers!")
    except Exception as e:
        print('Error: ',e)
        await message.answer("Height must be positive numbers!")