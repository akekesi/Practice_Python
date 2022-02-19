# Happy Number
# https://en.wikipedia.org/wiki/Happy_number

from matplotlib import pyplot as plt


def func_is_happy(number: int, steps=100) -> list:
    """
    Check whether number is happy
    """
    numbers= [number]
    s = 0
    while numbers[-1] != 1:
        number_list = func_number_to_list(numbers[-1])
        number_new = 0
        for n in number_list:
            number_new += n**2
        numbers.append(number_new)
        if numbers[-1] in numbers[:-1]:
            print(f"{numbers[0]} is not happy number")
            return False, numbers
        s += 1
        if s > steps:
            print(f"{numbers[0]} is after {s} steps not happy number yet")
            print(f"sequence: {numbers}")
            return None, numbers
    print(f"{numbers[0]} is happy number")
    print(f"sequence: {numbers}")
    return True, numbers


def func_number_to_list(number: int) -> list:
    """
    Return digits of number a list
    """
    return [int(n) for n in str(number)]


def func_plot_list(numbers):
    """
    Plot sequence of happy number
    """
    fig, ax = plt.subplots()
    ax.plot(numbers, ".-k")
    if numbers[-1] == 1:
        ax.plot(len(numbers)-1, numbers[-1], ".g", markersize=13)
    else:
        ax.plot(len(numbers)-1, numbers[-1], ".r", markersize=13)
        ax.axhline(y=numbers[-1], color="r")
    plt.title("Happy Number")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # vaulue
    number = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12 ,13,
        19,
        490,
        555,
        989,
        998,
        1000
    ]

    # test
    for n in number:
        numbers = func_is_happy(n)
        print(numbers)
    numbers = func_is_happy(731)
    print(numbers)
    func_plot_list(numbers[-1])
