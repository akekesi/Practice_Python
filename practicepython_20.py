# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
# Extras:
#   1. Use binary search.


def func_is_in_list(list_inp: list, number_inp: int) -> bool:
    """
    Check whether number_np in list_inp    
    """
    if number_inp in list_inp:
        return True
    return False


def func_is_in_list_loop(list_inp: list, number_inp: int) -> bool:
    """
    Check whether number_np in list_inp
    """
    for l in list_inp:
        if number_inp == l:
            return True
    return False


def func_is_in_ordered_list_loop(list_inp: list, number_inp: int) -> bool:
    """
    Check whether number_np in ordered list_inp
    """
    for l in list_inp:
        if number_inp == l:
            return True
        if number_inp < l:
            return False
    return False


if __name__ == "__main__":
    # value
    list_inp = [
        [0,1,2,3,4,5,6,7,8,9],
        [0,3,6,9]
    ]
    number_inp = [0,1,2,3,4,5,6,7,8,9]

    # test
    for l in list_inp:
        for n in number_inp:
            is_in = func_is_in_list(l, n)
            print(f"{n}: {is_in}")
            if is_in != func_is_in_list_loop(l, n):
                print(f"something wrong")
            if is_in != func_is_in_ordered_list_loop(l, n):
                print(f"something wrong")