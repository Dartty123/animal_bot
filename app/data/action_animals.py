import json

from app.data import list_files, open_files


def remove_animal(animal_index: int) -> str:
    animals = open_files.get_animals()
    animal = animals.pop(animal_index)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    msg = f"Товар '{animal}' успішно видалено."
    return msg


def cure_animal_action(animal_index: int) -> str:
    animals = open_files.get_animals()
    animal = animals.pop(animal_index)

    cure_animal = open_files.get_cure_animal()
    cure_animal.append(animals)

    with open(list_files.CURE_ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(cure_animal, file)

    msg = f"Тварину '{animal}' успішно вилікувано. Дякую за відвідуваність."
    return msg


def add_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if animal in animals:
        msg = f"Тварина '{animal}' вже є у списку."
        return msg

    animals.append(animals)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    msg = f"Тварину '{animals}' успішно додано."
    return msg