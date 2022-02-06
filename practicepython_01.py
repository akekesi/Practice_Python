# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
#   1. Add on to the previous program by asking the user for another number
#      and printing out that many copies of the previous message.
#      (Hint: order of operations exists in Python)
#   2. Print out that many copies of the previous message on separate lines.
#      (Hint: the string "\n is the same as pressing the ENTER button)

import datetime


class Turn:

    def __init__(self, name: str, age: int, year=100) -> None:
        self.name = name
        self.age = age
        self.year = year
        diff = self.year - self.age
        self.text = f"{self.name} will turn {self.year} years old in {diff} years in {datetime.date.today().year + int(diff)}."

    def __str__(self) -> str:
        return self.text

    def func_multi_print(self, n=None) -> None:
        """
        Print text n times
        """
        if n == None:
            n = int(input("n: "))
        if n > 0:
            text = f"{1}. {self.text}"
            for i in range(1,n):
                text += f"\n{i+1}. {self.text}"
            print(text)


def main():
    """
    Return Turn class with inputs
    """
    name = input("your name: ")
    age = int(input("your age: "))
    year = int(input("year: "))

    return Turn(name, age, year)


if __name__ == "__main__":
    # value
    people = {
        "name": [
            "Attila",
            "Keki",
            "",
            None,
            13,
            "_"
        ],
        "age": [
            36,
            111,
            0,
            -13,
            2e3,
            0.52
        ],
    "n": [
            0,
            1,
            3,
            -1,
            2,
            4
        ]
    }

    # test
    for name, age, n in zip(people["name"], people["age"], people["n"]):
        tmp = Turn(name, age)
        print(tmp)
        tmp.func_multi_print(n)
        print("-------------")

    a = main()
    print(a)
    a.func_multi_print()
