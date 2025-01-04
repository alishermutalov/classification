from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
# internal packages
from loader import bot, dp
from keyboards.inline import race_btn, is_dangerous_btn, has_reason_btn
from utils.states import Alien
from config import TELEGRAM_GROUP_ID
from utils.formatting import group_formatter
from data.google_sheets import save_to_gsheet
from utils.id_generator import get_next_unique_number

@dp.callback_query(F.data.startswith("is_humanoid:"))
async def is_humanoid(call:CallbackQuery, state:FSMContext):
    answer = call.data.split(":")[1]
    if answer=="Yes":
        await state.update_data(humanoid=answer)
        await state.set_state(Alien.race)
        await call.message.edit_text(f"You selected: {answer}")
        await bot.send_message(chat_id=call.from_user.id, text="What is the alien race?", reply_markup=race_btn)
    else:
        await call.message.edit_text(f"You selected: {answer}")
        text = group_formatter({'type':'Alien', 'humanoid':'No'}, call.from_user.full_name)
        await bot.send_message(chat_id=TELEGRAM_GROUP_ID, text=text)
        
        
@dp.callback_query(Alien.race)
async def get_race(call:CallbackQuery, state:FSMContext):
    answer = call.data.split(":")[1]
    await state.update_data(race=answer)
    await state.set_state(Alien.skin)
    await call.message.edit_text(f"You selected: {answer}")
    await bot.send_message(chat_id=call.from_user.id, text="What is their skin color? (e.g., Green, Grey)")
    
@dp.message(Alien.skin)
async def get_skin_color(message:Message, state:FSMContext):
    await state.update_data(skin=message.text)
    await state.set_state(Alien.dangerous)
    await message.answer("Is the alien dangerous?", reply_markup=is_dangerous_btn)
    
@dp.callback_query(Alien.dangerous)
async def is_dangerous(call:CallbackQuery, state:FSMContext):
    answer = call.data.split(":")[1]
    await state.update_data(dangerous=answer)
    await state.set_state(Alien.has_reason)
    await call.message.edit_text(f"You selected: {answer}")
    await bot.send_message(chat_id=call.from_user.id, text="Does the alien have reason?", reply_markup=has_reason_btn)
    
@dp.callback_query(Alien.has_reason)
async def has_reason(call:CallbackQuery, state:FSMContext):
    answer = call.data.split(":")[1]
    await state.update_data(reason=answer)
    await state.set_state(Alien.weight)
    await call.message.edit_text(f"You selected: {answer}")
    await bot.send_message(chat_id=call.from_user.id, text="What is its weight in kg? (Enter a number in kg)")
    
@dp.message(Alien.weight)
async def get_weight(message:Message, state:FSMContext):
    try:
        if int(message.text)>0:
            await state.update_data(weight=int(message.text))
            await state.update_data(type="Alien")
            await state.update_data(id=f"#{get_next_unique_number()}")
            data = await state.get_data()
            await state.clear()
            text = group_formatter(data, message.from_user.full_name)
            await bot.send_message(chat_id=TELEGRAM_GROUP_ID, text=text)
            save_to_gsheet(data,message.from_user.full_name)
            await message.answer("All data saved!")
        else:
            await message.answer("Weight must be positiv number")
    except Exception as e:
        print('Error: ', e)
        await message.answer("Weight must be positiv number")