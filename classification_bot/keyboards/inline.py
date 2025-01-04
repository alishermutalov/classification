from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

type_of_being_btn = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Human", callback_data="init:human"),
    InlineKeyboardButton(text="Animal", callback_data="init:animal"),
    InlineKeyboardButton(text="Alien", callback_data="init:alien"),
]])

gender_btn = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Male", callback_data="gender:Male"),
    InlineKeyboardButton(text="Female", callback_data="gender:Female")
]])

is_humanoid_btn = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Yes", callback_data="is_humanoid:Yes"),
    InlineKeyboardButton(text="No", callback_data="is_humanoid:No"),
]])

education_btn = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Higher", callback_data="education:Higher"),
    InlineKeyboardButton(text="School", callback_data="education:School")
]])

is_mammal_btn = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Yes", callback_data="mammal:Yes"),
    InlineKeyboardButton(text="No", callback_data="mammal:No"),
]])

is_predator_btn = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Yes", callback_data="predator:Yes"),
    InlineKeyboardButton(text="No", callback_data="predator:No"),
]])

race_btn = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="X", callback_data="race:X"),
    InlineKeyboardButton(text="Y", callback_data="race:Y"),
    InlineKeyboardButton(text="Z", callback_data="race:Z")
]])

is_dangerous_btn = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Yes", callback_data="is_dangerous:Yes"),
    InlineKeyboardButton(text="No", callback_data="is_dangerous:No"),
]])

has_reason_btn = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Yes", callback_data="has_reason:Yes"),
    InlineKeyboardButton(text="No", callback_data="has_reason:No"),
]])