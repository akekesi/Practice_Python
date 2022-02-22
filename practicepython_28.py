# https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html
# Implement a function that takes as input three variables, and returns the largest of the three.
# Do this without using the Python max() function!
# The goal of this exercise is to think about some internals that Python normally takes care of for us.
# All you need is some variables and if statements!


def func_max(numbers: list) -> float:
    """
    Return max value from list of numbers without max()
    """
    max_number = float("-inf")
    for n in numbers:
        if n > max_number:
            max_number = n
    return max_number


if __name__ == "__main__":
    # value
    numbers = [
        [0, 1, 2, 3],
        [-1, 0, -11, 99, 0,99],
        [-99.9, -10.10, -0.000001],
        [0, 0, 0, -0.000001],
        [0, 0, 0, float("inf"), 999]
    ]

    # test
    for n in numbers:
        max_number = func_max(n)
        print(max_number)
