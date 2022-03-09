# https://www.practicepython.org/exercise/2022/03/20/39-character-input-datetime.html
# Implement the same exercise as Exercise 1 (Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old),
# except don’t explicitly write out the year.
# Use the built-in Python datetime library to make the code you write work during every year, not just the one we are currently in.

from practicepython_01 import Turn
from practicepython_01 import main

if __name__ == "__main__":
    a = Turn("Otto", 27)
    print(a)

    b = main()
    print(b)
