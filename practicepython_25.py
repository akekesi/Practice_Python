# https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html
# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
# At the end of this exchange, your program should print out how many guesses it took to get your number.
# As the writer of this program, you will have to choose how your program will strategically guess.
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
# But that’s not an optimal guessing strategy.
# An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed.
# After you’ve written the program, try to find the optimal strategy!
# (We’ll talk about what is the optimal one next week with the solution.)


class Guess:

    def __init__(self, intervall=[0,100]) -> None:
        self.intervall = list(range(intervall[0], intervall[1]+1))

    def func_guess(self) -> int:
        """
        Play guess
        """
        guesses = 1
        intervall = self.intervall
        mitte = int(len(self.intervall)/2)
        guess = intervall[mitte]
        answer = input(f"{guess} ")
        while answer != "=":
            if answer == "<":
                intervall = intervall[:mitte]
            elif answer == ">":
                intervall = intervall[mitte:]
            else:
                print("wrong input")
                guesses -=1
            mitte = int(len(intervall)/2)
            try:
                guess = intervall[mitte]
            except IndexError as e:
                print(f"something wrong\n{e}")
            answer = input(f"{guess} ")
            guesses += 1
        print(f"{guess} --> WIN <-- {guess}\n(guesses: {guesses})")
        return guess


if __name__ == "__main__":
    # value
    intervall = [
        [7,52],
        [1,15],
        [1,1]
    ]

    # test
    game = Guess()
    print(f"intervall:\n{game.intervall}")
    game.func_guess()

    for i in intervall:
        game = Guess(i)
        print(f"intervall:\n{game.intervall}")
        game.func_guess()
