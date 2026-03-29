def get_int(prompt: str):
    value = None
    while value == None:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Enter a numeric option greater than zero")
        except ValueError as e:
            print(e)
    return value


def get_str(prompt: str):
    text = None
    while not text:
        text = input(prompt).strip()
    return text.lower()


def ask_y_n(prompt: str):
    option = None
    while option not in ("y", "n"):
        option = input(f"{prompt} type (y or n): ").strip().lower()
    return option == "y"
