# https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html
# This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.
# As you may have guessed, we are trying to build up to a full tic-tac-toe board.
# However, this is significantly more than half an hour of coding, so we’re doing it in pieces.
# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.
# If a game of Tic Tac Toe is represented as a list of lists, like so:
# game = [[1, 2, 0],
# 	      [2, 1, 0],
# 	      [2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space,
# and a 2 means that player 2 put their token in that space.
# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
# tell me whether anyone has won, and tell me which player won, if any.
# A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.
# Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
# Here are some more examples to work with:
# winner_is_2 = [[2, 2, 0],
# 	             [2, 1, 0],
# 	             [2, 1, 1]]
# winner_is_1 = [[1, 2, 0],
# 	             [2, 1, 0],
# 	             [2, 1, 1]]
# winner_is_also_1 = [[0, 1, 0],
# 	                  [2, 1, 0],
# 	                  [2, 1, 1]]
# no_winner = [[1, 2, 0],
#              [2, 1, 0],
# 	           [2, 1, 2]]
# also_no_winner = [[1, 2, 0],
# 	                [2, 1, 0],
# 	                [2, 1, 0]]

import numpy as np


def func_check_tictactoe(list_to_check: list) -> tuple:
    """
    Check, whether anyone has won
    """
    list_to_check = np.array(list_to_check)
    n = len(list_to_check)
    mask = []
    mask.append(list_to_check == 1)
    mask.append(list_to_check == 2)
    masks = func_create_mask(n)
    # m = mask*masks[:,None] # 8x2x3x3
    # print("-->", np.shape(m))
    # print("-->", np.any(np.sum(m, axis=(2,3)) == 3)) # works too :)
    for i, m in enumerate(mask):
        # res_all = np.all(m == masks, axis=(1, 2)) # for case of existing every possible win mask 
        # res_any = np.any(res_all)                 # for case of existing every possible win mask
        for mask in masks:
            if np.sum(m*mask) == n:
                return True, i+1
    return False, 0


def func_create_mask(size_of_mask: int) -> list:
    """
    Return every win position as list of masks
    """
    masks = np.zeros((2*size_of_mask+2, size_of_mask, size_of_mask), dtype=bool)
    # horizontal
    for n in range(size_of_mask):
        masks[n][n] = np.ones((size_of_mask), dtype=bool)
    # vertical
    for n in range(size_of_mask, 2*size_of_mask):
        masks[n][:,n-size_of_mask] = np.ones((size_of_mask), dtype=bool)
    # diagonal
    for n in range(size_of_mask):
        masks[-2][n,n] = True
        masks[-1][n,-n-1] = True
    return masks


if __name__ == "__main__":
    # value
    size_of_mask = [2, 3, 4, 5]
    list_to_check = [
        [
            [0, 1, 2],
            [1, 2, 0],
            [2, 0, 1]
        ],
        [
            [1, 1, 2],
            [2, 1, 0],
            [2, 0, 1]
        ],
        [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ],
        [
            [1, 2, 2],
            [2, 1, 2],
            [2, 1, 2]
        ],
        [
            [2, 1, 2],
            [2, 2, 1],
            [1, 2, 1]
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        # this cannot occur during the game
        [
            [1, 1, 1],
            [2, 2, 2],
            [2, 2, 2]
        ],
    ]

    # test
    for s in size_of_mask:
        masks = func_create_mask(s)
        print(masks)
    for l in list_to_check:
        res = func_check_tictactoe(l)
        print(res)
