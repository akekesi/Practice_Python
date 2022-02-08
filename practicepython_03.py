# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
# Extras:
#   1. Instead of printing the elements one by one,
#      make a new list that has all the elements less than 5 from this list in it and print out this new list.
#   2. Write this in one line of Python.
#   3. Ask the user for a number and return a list that contains only elements from the original list a
#      that are smaller than that number given by the user.

import numpy as np


class LessThen:

    def __init__(self, a: list, number=5) -> None:
        self.a = np.array(a)
        self.number = number
        self.text = self.func_text()

    def __str__(self) -> str:
        return self.text

    def func_less_then(self, number: float) -> list:
        """
        Return list that contains numbers smaller than number
        
        """
        mask = self.a < number
        return self.a[mask]

    def func_text(self) -> str:
        """
        Create string from list from func_less_then()
        """
        text = ""
        for i, n in enumerate(self.func_less_then(self.number)):
            if i == 0:
                text = f"{n}"
            else:
                text += f", {n}"
        return text


if __name__ == "__main__":
    # value
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # test
    less_then = LessThen(a)
    print(less_then)
    less_then_3 = less_then.func_less_then(22)
    print(less_then_3)
