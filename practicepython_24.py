# https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.
# Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- --- 
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
# Remember that in Python 3, printing to the screen is accomplished by
#   print("Thing to show on screen")
# Hint: this requires some use of functions,
# as were discussed previously on this blog and elsewhere on the Internet, like this TutorialsPoint link.


def func_print_game_board(values: list) -> str:
    """
    Return game board filled with values
    """
    number_columns = len(values[0])
    h = " ---" * number_columns
    board = ""
    for row in values:
        board += h
        tmp_row = ""
        for r in row:
            tmp_row += f"| {r} "
        tmp_row += "|"
        board += "\n" + tmp_row + "\n"
    board += h
    return board


if __name__ == "__main__":
    #value
    value = [
        [[" "]],
        [[1]],
        [[1, 2]],
        [[1, 2], [3, 4]],
        [[1, 2, 3], [4, 5, 6]],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3, 4], [5, 6, 7, 8]],
        [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    ]

    # test
    for v in value:
        print("++++++++++++++++++++++++++")
        board = func_print_game_board(v)
        print(board)
