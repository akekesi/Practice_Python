# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
# Extras:
#   1. Keep the game going until the user types “exit”
#   2. Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random


class GuessNumber:

    def __init__(self, number_min=1, number_max=9) -> None:
        self.nummber_min = number_min
        self.nummber_max = number_max

    def func_play(self, guess: int) -> str:
        """
        Check wheter guess is too low, too high, or exactly right
        """
        computer = random.randint(self.nummber_min, self.nummber_max)
        if guess > computer:
            text = ">"
        elif guess < computer:
            text = "<"
        else:
            text = "="
        return f"{guess} {text} {computer}"

    def func_plays(self) -> None:
        """
        Play until guess="exit"
        """
        point = 0
        while True:
            guess = input("Your guess: ")
            if guess == "exit":
                print(f"Points: {point}")
                return None
            try:
                text = self.func_play(int(guess))
                if "=" in text:
                    point += 1
                print(text)
            except ValueError as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    # value
    guess_1 = list(range(1,10))
    guess_2 = [5]*13

    # test
    game = GuessNumber()
    for g_1, g_2 in zip(guess_1, guess_2):
        print(game.func_play(g_1))
        print(game.func_play(g_2))
    game.func_plays()