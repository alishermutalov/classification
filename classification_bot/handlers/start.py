from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram import F
from aiogram.fsm.context import FSMContext

from loader import bot, dp
from keyboards.inline import type_of_being_btn, gender_btn, is_humanoid_btn
from utils.states import Human, Animal
    
@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Use /classify to start the classification process!")
    
@dp.message(Command("classify"))
async def classify_command(message: Message):
    await message.answer("What type of being?", reply_markup=type_of_being_btn)
    
@dp.callback_query(F.data.startswith("init"))
async def choosing_type(call:CallbackQuery, state:FSMContext):
    being_type = call.data.split(':')[1]
    
    if being_type == 'human':
        await call.message.edit_text(f"You selected: {being_type.capitalize()}")
        await state.set_state(Human.gender)
        await bot.send_message(chat_id=call.from_user.id, text="What is your GENDER?", reply_markup=gender_btn)
    elif being_type == 'animal':
        await call.message.edit_text(f"You selected: {being_type.capitalize()}")
        await state.set_state(Animal.species)
        await bot.send_message(chat_id=call.from_user.id, text="What species is it? (e.g., Dog, Cat)")
    else:
        await call.message.edit_text(f"You selected: {being_type.capitalize()}")
        await bot.send_message(chat_id=call.from_user.id, text="Is it humanoid?", reply_markup=is_humanoid_btn)
        
        
