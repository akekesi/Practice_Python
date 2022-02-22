# https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html
# In a previous exercise we explored the idea of using a list of lists as a “data structure” to store information about a tic tac toe game.
# In a tic tac toe game, the “game server” needs to know where the Xs and Os are in the board,
# to know whether player 1 or player 2 (or whoever is X and O won).
# There has also been an exercise about drawing the actual tic tac toe gameboard using text characters.
# The next logical step is to deal with handling user input. When a player (say player 1, who is X) wants to place an X on the screen,
# they can’t just click on a terminal. So we are going to approximate this clicking simply by asking the user for a coordinate of where they want to place their piece.
# As a reminder, our tic tac toe game is really a list of lists. The game starts out with an empty game board like this:
# game = [[0, 0, 0],
# 	      [0, 0, 0],
# 	      [0, 0, 0]]
# The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3. Then the game would print out
# game = [[0, 0, X],
#         [0, 0, 0],
# 	      [0, 0, 0]]
# And ask Player 2 for their move, printing an O in that place.
# Things to note:
# For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
# Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0). To people who don’t program,
# starting to count at 0 is a strange concept, so it is better for the user experience if the row counts and column counts start at 1.
# This is not required, but whichever way you choose to implement this, it should be explained to the player.
# Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number.
# Then you can use your Python skills to figure out which row and column they want their piece to be in.
# Don’t worry about checking whether someone won the game,
# but if a player tries to put a piece in a game position where there already is another piece, do not allow the piece to go there.
# Bonus:
# For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full.
# In a bonus version, keep track of how many squares are full and automatically stop asking for moves when there are no more valid moves.


def func_set_sign(game_board: list, row: int, column: int, sign: str) -> bool:
    """
    Set the sign in game_board if possible
    """
    row -= 1
    column -= 1
    try:
        if game_board[row][column] == " ":
            game_board[row][column] = sign
            return True
        else:
            print(f"contained, choose an other spot")
            return False
    except:
        print(f"something wrong")
        return False


def func_game() -> str:
    """
    Play game until game_board is full
    """
    game_board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    sign = ["x", "o"]
    player = [1, 2]
    r = 0
    print(f"round-{r}: {game_board}")
    while r < 9:
        inp = input(f"P{player[r % 2]}(row, column): ")
        [row, column] = [int(i) for i in inp.split(",")]
        if func_set_sign(game_board, row, column, sign[r % 2]):
            # check whether someone won
            r += 1
        print(f"round-{r}: {game_board}")


if __name__ == "__main__":
    # value
    game_board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    row = 1
    column = 1
    sign = "x"

    # test
    for r in range(1,4):
        for c in range(1, 4):
            func_set_sign(game_board, r, c, sign)
            print(game_board)
    func_set_sign(game_board, row, column, sign)
    print(game_board)

    func_set_sign(game_board, 1.3, column, sign)
    print(game_board)

    func_game()
