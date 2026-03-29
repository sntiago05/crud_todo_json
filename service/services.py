from model.dict_structure import TodoTask, TodoTaskInput, TodoTaskUpdate
from typing import NoReturn


def create_note(notes: list[TodoTask], note: TodoTaskInput):
    if any((v is None for v in note.values())):
        raise ValueError("Any value is None")
    new_note: TodoTask = {
        "id": generate_id(notes),
        "title": note["title"],
        "content": note["content"],
        "completed": False,
    }
    notes.append(new_note)
    return notes


def show_notes(notes: list[TodoTask]):
    if not notes:
        raise_empty_notes_error()
    return "\n".join(show_single_note(n) for n in notes)


def show_single_note(note: TodoTask):
    return (
        f"{note['id']} - {note['title']}\n{note['content']}\nstate: {note['completed']}"
    )


def search_note_by_id(notes: list[TodoTask], id: int):
    return next((n for n in notes if n["id"] == id), None)


def generate_id(notes: list[TodoTask]) -> int:
    return max((n["id"] for n in notes), default=0) + 1


def update_note(notes: list[TodoTask], updates: TodoTaskUpdate, id: int):
    if not notes:
        raise_empty_notes_error()
    exist = search_note_by_id(notes, id)
    if not exist:
        raise_note_not_found()

    for k, v in updates.items():
        exist[k] = v

    return notes


def delete_by_id(notes: list[TodoTask], id: int):
    if not notes:
        raise_empty_notes_error()
    to_delete = search_note_by_id(notes, id)
    if not to_delete:
        raise_note_not_found()
    notes.remove(to_delete)
    return notes


def raise_empty_notes_error() -> NoReturn:
    raise ValueError("Notes are empty")


def raise_note_not_found() -> NoReturn:
    raise ValueError("Note not found")
