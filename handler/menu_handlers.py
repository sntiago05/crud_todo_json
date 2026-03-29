from repository.repository import save_notes, load_notes
from service.services import (
    search_note_by_id,
    create_note,
    delete_by_id,
    update_note,
    show_notes,
    raise_note_not_found,
    show_single_note,
)
from model.dict_structure import TodoTask, TodoTaskInput, TodoTaskUpdate
from utils.get_values import get_str, get_int, ask_y_n


def handle_add_note():
    note: TodoTaskInput = {
        "title": get_str("enter the title: "),
        "content": get_str("enter the content: "),
    }
    try:

        notes: list[TodoTask] = load_notes()
        save_notes(create_note(notes, note))
        print("Note create successfully")
    except ValueError as e:
        print(e)
    except FileNotFoundError as fn:
        print(f"File not found {fn}")
    except Exception as e:
        print(f"an unexpected error occurred {e}")


def handle_show_notes():
    try:
        notes: list[TodoTask] = load_notes()
        print(show_notes(notes))
    except ValueError as e:
        print(e)


def handle_search_note():
    try:
        notes: list[TodoTask] = load_notes()
        note: TodoTask | None = search_note_by_id(
            notes, get_int("Enter the id to search: ")
        )
        if not note:
            raise_note_not_found()
        print(show_single_note(note))
    except ValueError as e:
        print(e)
    except Exception as ex:
        print(f"An unexpected error ocurred: {ex}")


def handle_update_note():
    id = get_int("Enter the id to update: ")
    try:
        notes: list[TodoTask] = load_notes()
        updates: TodoTaskUpdate = {}
        if ask_y_n("Do you want to update the title?"):
            updates["title"] = get_str("Enter the title: ")
        if ask_y_n("Do you want to update the content?"):
            updates["content"] = get_str("Enter the content: ")
        if ask_y_n("Do you want to update the state?"):
            updates["completed"] = ask_y_n("Is the note complete?")
        save_notes(update_note(notes, updates, id))
        print("Note update successfully")
    except FileNotFoundError as fn:
        print(f"File not found {fn}")
    except ValueError as e:
        print(e)
    except Exception as ex:
        print(f"An unexpected error ocurred: {ex}")


def handle_delete_note():
    try:
        notes = load_notes()
        save_notes(delete_by_id(notes, get_int("Enter the id to delete: ")))
        print("Note deleted")
    except FileNotFoundError:
        print("File not found")
    except ValueError as e:
        print(e)
    except Exception as ex:
        print(f"An unexpected error ocurred: {ex}")


def handle_exit():
    print("Good bye")
