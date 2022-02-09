# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)


def func_palindrome(text: str) -> str:
    """
    Check wether text is palindrome
    """
    half = int(len(text) / 2)
    text_1 = text[:half]
    text_2 = text[::-1][:half]
    if text_1 == text_2:
        return f"{text} is palindrome"
    return f"{text} is not palindrome"


if __name__ == "__main__":
    text = ["abcde", "abcba", "abba", "a", "", "abcde edcba"]
    for t in text:
        print(func_palindrome(t))