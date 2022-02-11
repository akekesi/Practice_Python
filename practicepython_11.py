# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.

import numpy as np


def func_is_prime(number: int) -> bool:
    """
    Check whether number is prime
    """
    if number < 2:
        return False
    for i in range(2,int(number**(1/2))+1):
        if number % i == 0:
            return False
    return True


def func_eratosthenes(number_min: int, number_max: int) -> list:
    """
    Return list of primes from number_min to number_max
    """
    prime = np.arange(number_max + 1)
    mask = np.ones(np.shape(prime), dtype=bool)
    mask[:2] = False
    for i in range(2, int(number_max**(1/2))+1):
        if mask[i]:
            for j in range (i*i, number_max+1, i):
                mask[j] = False
    mask[:number_min] = False
    return prime[mask]


if __name__ == "__main__":
    # value
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 199]

    # test
    for n in number:
        text_prime = ""
        if func_is_prime(n):
            text_prime = "--> prime"
        print(f"{n} {text_prime}")

    print("---------------------------------------")
    # value
    number_min = [0, 1, 2, 3, 4, 5, 13, 199, 13, 14]
    number_max = [13, 13, 13, 13, 13, 13, 50, 199, 0, 16]

    # test
    for n_min, n_max in zip(number_min, number_max):
        prime = func_eratosthenes(n_min, n_max)
        print(f"primes from {n_min} to {n_max}:\n{prime}")
        print("---------------------------------------")
