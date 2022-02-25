# https://www.practicepython.org/exercise/2017/01/10/32-hangman.html
# This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 2.
# In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.
# In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. In this exercise, we have to put it all together and add logic for handling guesses.
# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
# Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
# Optional additions:
# When the player wins or loses, let them start a new game.
# Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. This is challenging - do the other parts of the exercise first!
# Your solution will be a lot cleaner if you make use of functions to help you!

# Hangman class is already impemented in practicepython_31.py

from practicepython_30 import func_read_file
from practicepython_30 import func_random_from_list
from practicepython_31 import Hangman


if __name__ == "__main__":
    # value
    path = r"C:\00_TUBI\99_GIT\Practice_Python\practicepython_30_SOWPODS.txt"

    # test
    list_pw = func_read_file(path)
    password = func_random_from_list(list_pw)
    print(password)
    hangman_1 = Hangman(password)
    hangman_1.func_game()
    hangman_1.func_new_game(rounds=6)
    hangman_1.func_new_game(password="ABC", rounds=6)
