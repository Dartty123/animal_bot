import json

from app.data import list_files, open_files


def remove_animal(animal_index: int) -> str:
    animals = open_files.get_animals()
    animal = animals.pop(animal_index)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    msg = f"Товар '{animal}' успішно видалено."
    return msg


def CURE_ANIMALS(animal_index: int) -> str:
    animals = open_files.get_animals()
    animal = animals.pop(animal_index)

    CURE_ANIMALS = open_files.get_animals()
    CURE_ANIMALS.append(animal)

    with open(list_files.CURE_ANIMALS, "aw", encoding="utf-8") as file:
        json.dump(animals, file)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(CURE_ANIMALS, file)

    msg = f"Твариу '{animal}' успішно вилікувано. Дякую за відвідуваність."
    return msg


def add_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if animal in animals:
        msg = f"Тварина '{animal}' вже є у списку."
        return msg

    animals.append(animal)

    with open(list_files.animalS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    msg = f"Тварину  '{animal}' успішно додано."
    return msg