# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# Extras:
#   1. IWrite two different functions to do this - one using a loop and constructing a list, and another using sets.
#   2. Go back and do Exercise 5 using sets, and write the solution for that in a different function.

import random


def func_remove_duplicate(list_old: list) -> list:
    """
    Return list without duplicates
    """
    length = len(list_old)
    list_new = []
    for i in range(length):
        if list_old[i] not in list_new:
            list_new.append(list_old[i])
    return list_new


if __name__ == "__main__":
    # value
    number_min = 0
    number_max = 9
    list_min = 0
    list_max = 10
    test = 5

    # test
    for _ in range(test):
        list_old = [random.randint(number_min, number_max) for _ in range(random.randint(list_min, list_max))]
        list_new = (func_remove_duplicate(list_old))
        if set(list_old) == set(list_new):
            print(f"list old: {list_old}")
            print(f"list new: {list_new}")
        else:
            print("something wrong")
