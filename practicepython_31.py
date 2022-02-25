# https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html
# This exercise is Part 2 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 3.
# Let’s continue building Hangman. In the game of Hangman,
# a clue word is given by the program that the player has to guess, letter by letter.
# The player guesses one letter at a time until the entire word has been guessed.
# (In the actual game, the player can only guess 6 letters incorrectly before losing).
# Let’s say the word the player has to guess is “EVAPORATE”.
# For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly.
# For now, let the player guess an infinite number of times until they get the entire word.
# As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again.
# Remember to stop the game when all the letters have been guessed correctly!
# Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining - we will deal with those in a future exercise.
# An example interaction can look like this:
# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...
# And so on, until the player gets the word.


class Hangman:

    def __init__(self, password) -> None:
        self.password = password.upper()
        self.board = ["_"] * len(password)
        self.guesses = []
        self.pos = []

    def func_guess(self, rounds: int) -> None:
        """
        Append input to self.guesses
        """
        self.guesses.append(input(f"guess-{rounds}: ").upper())

    def func_pos_in_string(self):
        """
        Append position of last guess to self.pos
        """
        self.pos.append([i for i, x in enumerate(self.password) if x == self.guesses[-1]])

    def func_set(self) -> None:
        """
        Write last guess in self.board
        """
        for i in self.pos[-1]:
            self.board[i] = self.guesses[-1]

    def func_game(self, rounds=float("inf")) -> bool:
        """
        Play game
        """
        print(f"---START---")
        print(f"{self.board}")
        r = 0
        while r < rounds:
            r += 1
            self.func_guess(rounds=r)
            self.func_pos_in_string()
            if self.guesses[-1] == self.password:
                text_win = self.func_print(r)
                print(text_win)
                return True
            self.func_set()
            print(f"{self.board}")
            if "_" not in self.board:
                text_win = self.func_print(r)
                print(text_win)
                return True
        text_win = self.func_print(r, win=False)
        print(text_win)
        return False

    def func_new_game(self, password=False, rounds=float("inf")) -> None:
        """
        Play new game
        """
        if password:
            self.password = password
        self.board = ["_"] * len(self.password)
        self.guesses = []
        self.pos = []
        self.func_game(rounds=rounds)

    def func_print(self, rounds: int,  win=True) -> str:
        """
        Return win/lose text
        """
        if win:
            return f"---WIN---\nrounds: {rounds}\npassword: {self.password}"
        return f"---LOSE---\nrounds: {rounds}"


if __name__ == "__main__":
    # value
    string = [
        "ABC",
        "ABCDDCBA"
    ]

    # test
    for s in string:
        hangman = Hangman(s)
        hangman.func_game()
        hangman.func_new_game(rounds=6)
        hangman.func_new_game(password="A")
        hangman.func_new_game(password="A", rounds=2)
