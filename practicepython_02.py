# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
# Extras:
#   1. If the number is a multiple of 4, print out a different message.
#   2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#      If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


class Number:

    def __init__(self, number: int, divider=4) -> None:
        try:
            self.number = int(number)
            self.divider = int(divider)
        except ValueError:
            print(f"Input {number} can't be converted to integer.")
        self.text = self.func_text()

    def __str__(self) -> str:
        return self.text

    def func_is_even(self) -> int:
        """
        https://www.youtube.com/watch?v=BsD2aLsFo3E&t=393s
        Return:
            0:  even
            1:  odd
        """
        return self.number & 1

    def func_is_multiple(self) -> int:
        """
        Check if self.number is multiple of divider
        Return:
            0:  not dividable
            1:  dividable
        """
        if self.number % self.divider == 0:
            return 1
        return 0

    def func_text(self) -> str:
        """
        Return text
        """
        if self.func_is_multiple():
            text_prefix = f", and"
        else:
            text_prefix = f", but not"
        
        text_multiple = f"{text_prefix} multiple of {self.divider}"
        
        if not self.func_is_even():
            text = f"even{text_multiple}"
        else:
            text = f"odd{text_multiple}"
        return f"The number {self.number} is {text}"


if __name__ == "__main__":
    # value
    number = [0, 1, 2, 3, 99, 1e3, -1, -44, 1.3, "52", True, False] # , "STRING"]   # --> error
    divider = [1, 2, 3, 4, 5, 6, 7, 10, 13, -1, -11]                # , 0]          # --> error

    # test
    for n in number:
        number = Number(n)
        print(number)
    print("----------------------------------------------------")
    for d in divider:
        number = Number(number=77, divider=d)
        print(number)
    print("----------------------------------------------------")
    for d in divider:
        number = Number(number=78, divider=d)
        print(number)
