# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
# Extras:
#   1. Randomly generate two lists to test this
#   2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random
import numpy as np


def func_common(list_1: list, list_2: list) -> list:
    """
    Return list of elements that are common between the list_1 und list_2 (without duplicates) 
    
    """
    common = []
    if len(list_1) > len(list_2):
        list_1, list_2 = list_2, list_1
    for element in list_1:
        if element in list_2 and element not in common:
            common.append(element)
    return common


def func_test(list_1: list, list_2: list) -> None:
    """
    Test func_common
    """
    common = func_common(list_1, list_2)
    common_check = np.intersect1d(list_1, list_2)
    if set(common) == set(common_check):
        print(f"list_1: {list_1}\nlist_2: {list_2}")
        print(f"common: {common}")
    else:
        print(f"something wrong")


if __name__ == "__main__":
    # value
    list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # test
    func_test(list_1, list_2)

    print("----------------------------------------------------")
    # value
    number_min = 0
    number_max = 13
    list_min = 0
    list_max = 13
    list_1 = [random.randint(number_min, number_max) for _ in range(random.randint(list_min, list_max))]
    list_2 = [random.randint(number_min, number_max) for _ in range(random.randint(list_min, list_max))]

    # test
    func_test(list_1, list_2)

    print("----------------------------------------------------")
    # value
    number_min = 0
    number_max = 13
    list_min = 0
    list_max_1 = 13
    list_max_2 = 1
    list_1 = [random.randint(number_min, number_max) for _ in range(random.randint(list_min, list_max_1))]
    list_2 = [random.randint(number_min, number_max) for _ in range(random.randint(list_min, list_max_2))]

    # test
    func_test(list_1, list_2)
