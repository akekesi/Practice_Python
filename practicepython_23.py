# https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000,
# and the other .txt file has a list of happy numbers up to 1000.
# (If you forgot, prime numbers are numbers that can’t be divided by any other number.
# And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.
# The explanation is easier with an example, which I will describe below.)


def func_read_file(path: str) -> str:
    """
    Read text and return lines as list
    """
    try:
        with open(path, 'r') as f:
            return f.read().splitlines()
    except OSError as e:
        text_error = f"something wrong\n{e}"
        print(text_error)


def func_remove_space(list_to_change):
    """
    Remove space from string
    """
    return [l.split()[0] for l in list_to_change]


def func_common(list_1, list_2, integer=False):
    """
    Return common elements from two lists
    """
    list_3 = []
    if len(list_1) > len(list_2):
        list_1, list_2 = list_2, list_1
    for l in list_1:
        if l in list_2:
            if integer:
                l = int(l)
            list_3.append(l)
    return list_3


if __name__ == "__main__":
    # value
    path_prime = r"C:\00_TUBI\99_GIT\Practice_Python\practicepython_23_text_prime.txt"
    path_happy = r"C:\00_TUBI\99_GIT\Practice_Python\practicepython_23_text_happy.txt"

    # test
    list_prime = func_remove_space(func_read_file(path_prime))
    print(list_prime)
    list_happy = func_remove_space(func_read_file(path_happy))
    print(list_happy)
    list_common = func_common(list_prime, list_happy)
    print(list_common)
    list_common_int = func_common(list_prime, list_happy, integer=True)
    print(list_common_int)
