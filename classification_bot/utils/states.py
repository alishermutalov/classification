from aiogram.fsm.state import State, StatesGroup


class Human(StatesGroup):
    gender = State()
    age = State()
    nationality = State()
    education = State()
    eye_color = State()
    hair_color = State()
    height = State()
    
    
class Animal(StatesGroup):
    species = State()
    mammal = State()
    predator = State()
    color = State()
    weight = State()
    age = State()
    

class Alien(StatesGroup):
    race = State()
    skin = State()
    dangerous = State()
    has_reason = State()
    weight = State()
   