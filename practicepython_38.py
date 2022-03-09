# https://www.practicepython.org/exercise/2022/03/06/38-f-strings.html
# Implement the same exercise as Exercise 1 (Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old),
# except use f-strings instead of the + operator to print the resulting output message.

from practicepython_01 import Turn
from practicepython_01 import main

if __name__ == "__main__":
    a = Turn("Otto", 27)
    print(a)

    b = main()
    print(b)
