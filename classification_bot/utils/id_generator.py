LAST_USED_FILE = "last_used_number.txt"

def get_next_unique_number():
    try:
        with open(LAST_USED_FILE, "r") as file:
            last_number = int(file.read().strip())
    except FileNotFoundError:
        last_number = 9999

    next_number = last_number + 1
    with open(LAST_USED_FILE, "w") as file:
        file.write(str(next_number))

    return next_number
