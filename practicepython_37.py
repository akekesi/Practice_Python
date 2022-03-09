# https://www.practicepython.org/exercise/2022/02/20/37-functions-refactor.html
# One area of confusion for new coders is the concept of functions (which have been addressed on this blog in exercise 11 for example).
# So in this exercise, we will be stretching our functions muscle by refactoring an existing code snippet into using functions.
# Here is the code snippet to refactor (taken from a correct but very repeated solution to exercise 24 on this website):
# print(" --- --- ---")
# print("|   |   |   |")
# print(" --- --- ---")
# print("|   |   |   |")
# print(" --- --- ---")
# print("|   |   |   |")
# print(" --- --- ---")
# Hint: Think about a way to refactor this using functions where generating an 8x8 or a 19x19 grid is a single change to a function call!

from practicepython_24 import func_print_game_board


def func_empty_board_input(x: int = 3, y: int = 3) -> list:
    """
    Return list to create empty board
    """
    return [[" "] * x] * y


if __name__ == "__main__":
    # value
    x_list = [1, 2, 3, 7]
    y_list = [1, 2, 3]

    # test
    empty_board_input = func_empty_board_input()
    print(empty_board_input)
    board = func_print_game_board(empty_board_input)
    print(board)
    for y in y_list:
        for x in x_list:
            empty_board_input = func_empty_board_input(x, y)
            print(empty_board_input)
            board = func_print_game_board(empty_board_input)
            print(board)
