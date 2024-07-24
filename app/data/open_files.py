import os
import json

from app.data import list_files


if not os.path.exists(list_files.ANIMALS):
    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump([], file)

if not os.path.exists(list_files.CURE_ANIMALS):
    with open(list_files.CURE_ANIMALS, "w", encoding="utf-8") as file:
        json.dump([], file)

if not os.path.exists(list_files.REVIEWS):
    with open(list_files.REVIEWS, "w", encoding="utf-8") as file:
        json.dump([], file)


def get_ANIMALS(path: str = list_files.ANIMALS) -> list[str]:
    with open(path, "r", encoding="utf-8") as file:
        ANIMALS = json.load(file)

    return ANIMALS