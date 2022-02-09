# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner,
# and ask if the players want to start a new game)
# Remember the rules:
#   Rock beats scissors
#   Scissors beats paper
#   Paper beats rock

import random


class RockScissprsPaper:

    def __init__(self) -> None:
        self.rules = {
            "Rock": "Scissors",
            "Scissors": "Paper",
            "Paper": "Rock"
        }
        self.options = [*self.rules]
        self.wins = 0

    def func_play(self, hint: str) -> int:
        """
        Play with computer
        """    
        hint_comuter = random.choices(self.options, weights=(1, 1, 1), k=1)[0]
        text = "Computer win!"
        arr = "<--"
        win = 0
        if hint in ["Spock", "Lizard"]:
            print("Bazinga!")
            return win
        if self.rules[hint] == hint_comuter:
            text =  f"You win!"
            arr = "-->"
            win = 1
        elif hint == hint_comuter:
            text = f"Tied game"
            arr = f" = "
        print(f"{hint} {arr} {hint_comuter}")
        print(text)
        self.wins += win
        return win


if __name__ == "__main__":
    # test
    game = RockScissprsPaper()
    hint = random.choices(game.options, weights=(1, 1, 1), k=13)
    hint.append("Spock")
    hint.append("Lizard")
    for h in hint:
        game.func_play(h)
        print(f"All wins: {game.wins}")
        print("-------------")
