from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from loader import bot, dp
from keyboards.inline import is_mammal_btn, is_predator_btn
from utils.states import Animal
from config import TELEGRAM_GROUP_ID
from utils.formatting import group_formatter
from data.google_sheets import save_to_gsheet
from utils.id_generator import get_next_unique_number

@dp.message(StateFilter(Animal.species))
async def get_species(message:Message, state:FSMContext):
    await state.update_data(species=message.text)
    await state.set_state(Animal.mammal)
    await message.answer("Is it a mammal?", reply_markup=is_mammal_btn)
    
@dp.callback_query(Animal.mammal)
async def is_mammal(call:CallbackQuery, state:FSMContext):
    answer = call.data.split(":")[1]
    await state.update_data(mammal=answer)
    await state.set_state(Animal.predator)
    await call.message.edit_text(f"You selected: {answer}")
    await bot.send_message(chat_id=call.from_user.id, text="Is it a predator?", reply_markup=is_predator_btn)
    
@dp.callback_query(Animal.predator)
async def is_mammal(call:CallbackQuery, state:FSMContext):
    answer = call.data.split(":")[1]
    await state.update_data(predator=answer)
    await state.set_state(Animal.color)
    await call.message.edit_text(f"You selected: {answer}")
    await bot.send_message(chat_id=call.from_user.id, text="What is its primary color? (e.g., Brown, White)")
    
@dp.message(Animal.color)
async def get_color(message:Message, state:FSMContext):
    await state.update_data(color=message.text)
    await state.set_state(Animal.weight)
    await message.answer("What is its weight in kg? (Enter a number in kg)")
    
@dp.message(Animal.weight)
async def get_weight(message:Message, state:FSMContext):
    try:
        if int(message.text)>0:
            await state.update_data(weight=int(message.text))
            await state.set_state(Animal.age)
            await message.answer("How old is the animal in months? (Enter a number in months)")
        else:
            await message.answer("Weight must be positiv number")
    except:
        await message.answer("Weight must be positiv number")
    
@dp.message(Animal.age)
async def get_weight(message:Message, state:FSMContext):
    try:
        if int(message.text)>0:
            await state.update_data(age=int(message.text))
            await state.update_data(type="Animal")
            await state.update_data(id=f"#{get_next_unique_number()}")
            data = await state.get_data()
            await state.clear()
            text = group_formatter(data, message.from_user.full_name)
            await bot.send_message(chat_id=TELEGRAM_GROUP_ID, text=text)
            save_to_gsheet(data, message.from_user.full_name)
            await message.answer("All data saved!")
        else:
            await message.answer("Age must be positiv number")
    except Exception as e:
        await message.answer("Age must be positiv number")
        