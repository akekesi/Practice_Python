# https://www.practicepython.org/exercise/2022/04/03/40-error-checking.html
# Given this solution to Exercise 9, modify it to one level of user feedback:
# if the user does not enter a number between 1 and 9, tell them.
# Don’t count this guess against the user when counting the number of guesses they used.


def func_check_between(x_min: float = 0, x_max: float = 10) -> None:
    """
    Check input
    """
    while True:
        try:
            x = float(input(f"Guess an number (integer) between {x_min} and {x_max}: "))
            if x > x_min and x < x_max:
                print(f"{x_min} < {x} < {x_max}")
                return None
            else:
                print(f"number has to be between 1 and 9")
        except:
            print(f"something wrong")


if __name__ == "__main__":
    # test
    func_check_between()
    func_check_between(4, 6)
