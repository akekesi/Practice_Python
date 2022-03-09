# https://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html
# This exercise is Part 3 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 4.
# In the previous exercise we saved information about famous scientists’ names and birthdays to disk. In this exercise,
# load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.
# Your program should output something like:
# {
# 	"May": 3,
# 	"November": 2,
# 	"December": 1
# }

import json


def func_read_json(path: str) -> dict:
    """
    Read data from json
    """
    with open(path) as f:
        return json.load(f)


def func_print_dict(dictionary: dict) -> None:
    """
    Print dictionary
    """
    print(json.dumps(dictionary, indent=2, sort_keys=True))


def func_calc_months(dictionary: dict) -> str:
    """
    Count how many scientists have a birthday in each month
    """
    months = {}
    for v in dictionary.values():
        m = v.split("/")[1]
        if m not in months:
            months[m] = 0
        months[m] += 1
    return months


if __name__ == "__main__":
    # value
    path = r"C:\00_TUBI\99_GIT\Practice_Python\practicepython_34.json"

    # test
    data = func_read_json(path)
    func_print_dict(data)
    data["Edward Teller"] = "15/01/1908"
    data["Theodore von Karman"] = "11/05/1881"
    data["Alber Einstein"] = "14/03/1879"
    data["Richard Feynman"] = "11/05/1918"
    data["Stephen Hawking"] = "08/01/1942"
    func_print_dict(data)
    months = func_calc_months(data)
    func_print_dict(months)
