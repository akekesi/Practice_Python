# https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html
# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code,
# use the code from the solution),
# and instead of printing the results to a screen, write the results to a txt file.
# In your code, just make up a name for the file you are saving to.
# Extras:
#   1. Ask the user to specify the name of the output file that will be saved.

import os


def func_write_to_txt(text_to_write: str, dir_name="", file_name="text") -> None:
    """
    Write text_to_write in txt file
    """
    suffix = ".txt"
    path = os.path.join(dir_name, file_name + suffix)
    with open(path, 'w') as f:
        f.write(text_to_write)
        print(f"{path} saved")


if __name__ == "__main__":
    # value
    text_to_write = "test_0\ntest_1"
    dir_name = r"C:\Users\kekes\OneDrive\Desktop\delete"
    file_name = "test_file_name"
    suffix = ".txt"
    delete_txt = True

    # test
    func_write_to_txt(text_to_write)
    func_write_to_txt(text_to_write, dir_name=dir_name, file_name=file_name)

    # delete txt
    if delete_txt:
        path = "text.txt"
        os.remove(path)
        print(f"{path} deleted")

        path = os.path.join(dir_name, file_name + suffix)
        os.remove(path)
        print(f"{path} deleted")
