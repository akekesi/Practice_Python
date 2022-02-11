# https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
# This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
# Write this in one line of Python using at least one list comprehension.
# (Hint: Remember list comprehensions from Exercise 7).
# The original formulation of this exercise said to write the solution using one line of Python,
# but a few readers pointed out that this was impossible to do without using sets
# that I had not yet discussed on the blog, so you can either choose to use the original directive and read about the set command in Python 3.3,
# or try to implement this on your own and use at least one list comprehension in the solution.
# Extras:
#   1. Randomly generate two lists to test this

import random
import numpy as np
from practicepython_05 import func_common as func_common_05


def func_common(list_1: list, list_2: list) -> list:
    """
    Return list of elements that are common between the list_1 und list_2 (without duplicates) 
    
    """
    if len(list_1) > len(list_2):
        list_1, list_2 = list_2, list_1
    common = [element for element in set(list_1) if element in list_2]
    return common


def func_test(list_1: list, list_2: list) -> None:
    """
    Test func_common
    """
    common = func_common(list_1, list_2)
    common_05 = func_common_05(list_1, list_2)
    common_check = np.intersect1d(list_1, list_2)
    if set(common) == set(common_check) and set(common) == set(common_05):
        print(f"list_1:    {list_1}\nlist_2:    {list_2}")
        print(f"common:    {common}")
        print(f"common_05: {common}")
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
    common = func_common(list_1, list_2)
    common_05 = func_common_05(list_1, list_2)
    common_check = np.intersect1d(list_1, list_2)
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
    common = func_common(list_1, list_2)
    common_check = np.intersect1d(list_1, list_2)
    common_05 = func_common_05(list_1, list_2)
    func_test(list_1, list_2)
