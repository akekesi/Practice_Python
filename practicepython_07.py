# https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.


def func_even(list_input: list) -> list:
    """
    Return a list of even numbers from list_input
    """
    return [x for x in list_input if not x & 1] # https://www.youtube.com/watch?v=BsD2aLsFo3E&t=393s


if __name__ == "__main__":
    # value
    list_input = [
        [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],
        [1, 3, 5, 7, 9, 11, 13, 99],
        [0, 2, 4, 100],
        [-3, -2, -1, 0, 1, 2, 3],
        []
    ]

    # test
    for l in list_input:
        list_even = func_even(l)
        print(list_even)
