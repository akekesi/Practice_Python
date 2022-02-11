# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.


def func_first_last(list_inp: list) -> list:
    """
    Return the first and last element as list
    """
    return [list_inp[0], list_inp[-1]]


if __name__ == "__main__":
    # value
    list_inp = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [0, 1]
    ]

    # test
    for l in list_inp:
        print(func_first_last(l))
