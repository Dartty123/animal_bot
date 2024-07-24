from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.data import open_files, action_animals
from app.keyboards.animals import build_animals_keyboard, build_animal_actions_keyboard
from app.forms.animals import AnimalForm


animal_router = Router()


async def edit_or_answer(message: Message, text: str, keyboard=None, *args, **kwargs):
   if message.from_user.is_bot:
       await message.edit_text(text=text, reply_markup=keyboard, **kwargs)
   else:
       await message.answer(text=text, reply_markup=keyboard, **kwargs)


@animal_router.message(F.text == "Список тварин на лікувані")
async def show_animals(message: Message, state: FSMContext):
    animals = open_files.get_animals()
    keyboard = build_animals_keyboard(animals)
    await edit_or_answer(
        message=message,
        text="Список тварин на лікуван",
        keyboard=keyboard
    )


@animal_router.callback_query(F.data.startswith("animal_"))
async def animal_actions(call_back: CallbackQuery, state: FSMContext):
    animal_index = int(call_back.data.split("_")[-1])
    animal = open_files.get_animal(animal_index)
    keyboard = build_animal_actions_keyboard(animal_index)
    await edit_or_answer(
        message=call_back.message,
        text=animal,
        keyboard=keyboard
    )


@animal_router.callback_query(F.data.startswith("remove_animal_"))
async def remove_animal(call_back: CallbackQuery, state: FSMContext):
    animal_index = int(call_back.data.split("_")[-1])
    msg = action_animals.remove_animal(animal_index)
    await edit_or_answer(
        message=call_back.message,
        text=msg
    )


@animal_router.callback_query(F.data.startswith("cure_animal_"))
async def sold_animal(call_back: CallbackQuery, state: FSMContext):
    animal_index = int(call_back.data.split("_")[-1])
    msg = action_animals.sold_animal(animal_index)
    await edit_or_answer(
        message=call_back.message,
        text=msg
    )


@animal_router.message(F.text == "Показати список вилікуваних тварин")
async def shoe_sold_animal(message: Message, state: FSMContext):
    cure_animals = open_files.get_sold_animals()
    msg = ""
    for i, animal in enumerate(cure_animals, start=1):
        msg += f"{i}. {animal}\n"

    await message.answer(text=msg)


@animal_router.message(F.text == "Додати новий товар")
async def add_animal(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(AnimalForm.name)
    await edit_or_answer(
        message=message,
        text="Введіть назву товару"
    )


@animal_router.message(AnimalForm.name)
async def add_animal_name(message: Message, state: FSMContext):
    data = await state.update_data(name=message.text)
    await state.clear()
    msg = action_animals.add_animal(data.get("name"))
    await edit_or_answer(
        message=message,
        text=msg
    )