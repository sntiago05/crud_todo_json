import json
from model.dict_structure import TodoTask
import os

PATH = "./data/notes.json"


def save_notes(notes: list[TodoTask]):
    with open(PATH, mode="w", newline="") as file:
        json.dump(notes, file, indent=4)


def load_notes():
    if not os.path.exists(PATH):
        return []
    with open(PATH) as file:
        return json.load(file)
