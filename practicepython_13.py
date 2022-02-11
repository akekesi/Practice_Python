# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers
# where the next number in the sequence is the sum of the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def func_fibonacci_n(n: int) -> int:
    """
    Return the nth Fibonacci number
    """
    if n == 0:
        return 0
    if n < 3:
        return 1
    return func_fibonacci_n(n-1) + func_fibonacci_n(n-2)


def func_fibonacci_list(n: int) -> list:
    """
    Return the first n Fibonacci numbers as list
    """
    fibonacci_list = []
    for i in range(n+1):
        fibonacci_list.append(func_fibonacci_n(i))
    return fibonacci_list


if __name__ == "__main__":
    # value
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # test
    for n in number:
        print(func_fibonacci_n(n))
        print(func_fibonacci_list(n))
