#https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string:
# My name is Michele
# Then I would see the string:
# Michele is name My
# shown back to me.


def func_backwards_order(text: str) -> str:
    """
    Return text backwards ordered
    """
    return (" ").join(text.split(" ")[::-1])


if __name__ == "__main__":
    # value
    text = [
        "My name is Michele",
        "First Middle Last",
        "1 2 3 4 5",
        "abcde a"
    ]

    # test
    for t in text:
        text_rev = func_backwards_order(t)
        print(f"text old: {t}")
        print(f"text new: {text_rev}")
