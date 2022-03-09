# https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
# This exercise is Part 2 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 3, and Part 4.
# In the previous exercise we created a dictionary of famous scientists’ birthdays.
# In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk,
# rather than having the dictionary defined in the program.
# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary,
# and update the JSON file you have on disk with the scientist’s name.
# If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

import json
from practicepython_33 import Birthday


def func_read_json(path: str) -> dict:
    """
    Read data from json
    """
    with open(path) as f:
        return json.load(f)


def func_write_json(path: str, dict_to_json: dict) -> None:
    """
    Write data to json
    """
    with open(path, 'w') as f:
        json.dump(dict_to_json, f)


def func_print_dict(dictionary: dict) -> None:
    """
    Print dictionary
    """
    print(json.dumps(dictionary, indent=2, sort_keys=True))


if __name__ == "__main__":
    # value
    path = r"C:\00_TUBI\99_GIT\Practice_Python\practicepython_34.json"
    dictionary = {
        "Eugene Paul Wigner": "17/11/1902",
        "John von Neumann": "28/12/1903"
    }

    # test
    func_write_json(path, dictionary)
    data = func_read_json(path)
    func_print_dict(data)
    birthday = Birthday()
    birthday.func_new()
    birthday.func_print_names()
    func_print_dict(birthday.birthday)
    birthday.func_append_dict(dictionary)
    birthday.func_print_names()
    func_print_dict(birthday.birthday)
    birthday.func_print_birthday("Eugene Paul Wigner")
    birthday.func_print_names()
    func_print_dict(birthday.birthday)
