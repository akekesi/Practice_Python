# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


def func_divisors(number: int) -> list:
    """
    Return divisors of number
    """
    if number == 0:
        return f"every integer is divisor of {number}"
    d = [number]
    for n in range(int(number/2),0,-1):
        if number % n == 0:
            d.append(n)
    return d


if __name__ == "__main__":
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 199, 1_000, 1*2*3*4*5*6*7*8*9]
    for n in number:
        text_suffix = ""
        d = func_divisors(n)
        if len(d) == 2:
            text_suffix = f" --> {n} is prim"
        print(f"{n}:\t{d}{text_suffix}")
