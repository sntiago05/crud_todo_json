from handler.menu_handlers import (
    handle_add_note,
    handle_delete_note,
    handle_search_note,
    handle_show_notes,
    handle_update_note,
    handle_exit,
)
from utils.get_values import get_int

options = {
    1: handle_add_note,
    2: handle_show_notes,
    3: handle_search_note,
    4: handle_update_note,
    5: handle_delete_note,
    6: handle_exit,
}


def show_menu():
    print(
        """
========= MENU =========
1. Create note
2. Show notes
3. Search note by ID
4. Update note
5. Delete note
6. Exit
========================
"""
    )


def main():
    option = None
    while option != 6:
        show_menu()
        option = get_int("Choose an option: ")
        func = options.get(option)
        if func:
            func()
        else:
            print("Please enter a valid option")



main()
