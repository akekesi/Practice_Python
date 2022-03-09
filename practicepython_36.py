# https://www.practicepython.org/exercise/2017/04/02/36-birthday-plots.html
# This exercise is Part 4 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 3.
# In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.
# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in!
# Because it would take a long time for you to input the months of various scientists, you can use my scientist birthday JSON file.
# Just parse out the months (if you don’t know how, I suggest looking at the previous exercise or its solution) and draw your histogram.
# If you are using a purely web-based interface for coding, this exercise won’t work for you,
# since it requires installing the bokeh Python package.
# Now might be a good time to install Python on your own computer.

import matplotlib.pyplot as plt


def fun_plot_histogram(dictionary: dict) -> None:
    """
    Plot dict as histogram
    """
    x = dictionary.keys()
    y = dictionary.values()
    max_y = max(y)
    fig, ax = plt.subplots()
    ax.bar(x, y, width=1, edgecolor="white")
    plt.yticks(range(max_y+1))
    ax.set_xlabel('month')
    ax.set_ylabel('birthday')
    ax.set_title('birthday/month')
    plt.grid(axis="y")
    ax.set_axisbelow(True)
    plt.show()


if __name__ == "__main__":
    # value
    d = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 1
    }

    # test
    fun_plot_histogram(d)
