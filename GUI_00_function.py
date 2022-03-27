def func_test(value_1: str, value_2: float, value_3: str) -> float:
    """
    Print value_1, value_2 and value_3 and their type.
    Return 2 * value_2
    Args:
        value_1:    string
        value_2:    float
        value_3:    string
    Returns:
        2 * value_2
    """
    print(f"value_1: {value_1}, {type(value_1)}")
    print(f"value_2: {value_2}, {type(value_2)}")
    print(f"value_3: {value_3}, {type(value_3)}")
    return value_2*2


if __name__ == "__main__":
    # value
    value_1 = "a.bc"
    value_2 = 1.23
    value_3 = r"C:\Users\kekesati\Documents\GitHub\Practice_Python\GUI_00_file.txt"

    # test
    res = func_test(value_1=value_1, value_2=value_2, value_3=value_3)
    print(res)
