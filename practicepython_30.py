# https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
# This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and Part 3.
# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary.
# Download this file and save it in the same directory as your Python code.
# This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments.
# Each line in the file contains a single word.
# Hint: use the Python random library for picking a random word.

import random


def func_read_file(path: str) -> list:
    """
    Read text and return lines as list
    """
    try:
        with open(path, 'r') as f:
            return f.read().splitlines()
    except OSError as e:
        text_error = f"something wrong\n{e}"
        print(text_error)
        return []


def func_random_from_list(list_to_choice) -> str:
    """
    Pick a random element from list_to_choice
    """
    try:
        return random.choice(list_to_choice)
    except IndexError as e:
        text_error = f"something wrong\n{e}"
        print(text_error)


if __name__ == "__main__":
    # value
    path = [
        r"C:\00_TUBI\99_GIT\Practice_Python\practicepython_30_SOWPODS.txt",
        r"C:\00_TUBI\99_GIT\Practice_Python\wrong_path"
    ]

    # test
    for p in path:
        sowpods = func_read_file(p)
        random_choice = func_random_from_list(sowpods)
        print(random_choice)
