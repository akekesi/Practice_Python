# https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
# and print out the results to the screen.
# I have a .txt file for you, if you want to use it!
# Extras:
#   1. Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file,
#      and count how many of each “category” of each image there are.
#      This text file is actually a list of files corresponding to the SUN database scene recognition database,
#      and lists the file directory hierarchy for the images.
#      Once you take a look at the first line or two of the file, it will be clear which part represents the scene category.
#      To do this, you’re going to have to remember a bit about string parsing in Python 3.
#      I talked a little bit about it in this post.


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


def func_count_name(list_to_count: list) -> dict:
    """
    Count the names in list
    """
    count_dict = {}
    for l in list_to_count:
        if l in [*count_dict]:
            count_dict[l] += 1
        else:
            count_dict[l] = 1
    return count_dict


def func_count_category(list_to_count: list) -> dict:
    """
    Count the categories in list
    """
    count_dict = {}
    for l in list_to_count:
        l = "/".join([*l.split("/")[2:-1]])
        if l in [*count_dict]:
            count_dict[l] += 1
        else:
            count_dict[l] = 1
    return count_dict


if __name__ == "__main__":
    # value
    path_name = [
        r"C:\00_TUBI\99_GIT\Practice_Python\practicepython_22_text_name_1.txt",
        r"C:\00_TUBI\99_GIT\Practice_Python\not_exist.txt",
    ]
    path_category = [
        r"C:\00_TUBI\99_GIT\Practice_Python\practicepython_22_text_name_2.txt",
        r"C:\00_TUBI\99_GIT\Practice_Python\not_exist.txt",
    ]

    # test
    for p in path_name:
        list_text = func_read_file(p)
        if isinstance(list_text, list):
            count_dict = func_count_name(list_text)
            print(count_dict)

    for p in path_category:
        list_text = func_read_file(p)
        if isinstance(list_text, list):
            count_dict = func_count_category(list_text)
            print(count_dict)
