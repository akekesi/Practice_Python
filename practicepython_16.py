# https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
# Write a password generator in Python.
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.
# Extras:
#   1. Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random
import string


def func_pw_generator(length=4) -> str:
    """
    Return password that is a mix of lowercase letters, uppercase letters, numbers, and symbols
    """
    pw = ""
    while True:
        letter_l = random.choice(string.ascii_letters).lower()
        letter_u = random.choice(string.ascii_letters).upper()
        digit = random.choice(string.digits)
        punctuation  = random.choice(string.punctuation)
        options = [letter_l, letter_u, digit, punctuation]
        length_options = len(options)
        for n in range(length_options-1, -1, -1):
            if len(pw) == length:
                return pw
            pw += options.pop(random.randint(0,n))


if __name__ == "__main__":
    # value
    length = [0, 1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10]

    # test
    pw = func_pw_generator()
    print(pw)
    for l in length:
        pw = func_pw_generator(length=l)
        print(pw)
