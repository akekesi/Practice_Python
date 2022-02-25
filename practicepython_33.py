# https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
# This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are: Part 2, Part 3, and Part 4.
# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name.
# Create a dictionary (in your file) of names and birthdays.
# When you run your program it should ask the user to enter a name, and return the birthday of that person back to them.
# The interaction should look something like this:
# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.


class Birthday:

    def __init__(self) -> None:
        self.birthday = {}
        self.func_print_names()

    def func_new(self) -> None:
        """
        
        """
        name = input("name: ")
        date = "birthday: "
        self.birthday[name] = input(date)

    def func_print_names(self) -> None:
        """
        Print the names from dictionary
        """
        text_suffix = "We know the birthdays of:"
        if len(self.birthday) == 0:
            text_suffix = "The birthday dictionary is empty yet."
        print(f"Welcome to the birthday dictionary. {text_suffix}")
        for n in [*self.birthday]:
            print(n)

    def func_print_birthday(self, name=False) -> None:
        """
        Print the birthday of name
        """
        if not name:
            name = input("Who's birthday do you want to look up? ")
        if name in [*self.birthday]:
            print(f"{name}'s birthday: {self.birthday[name]}")
        else:
            print(f"No data about {name}")


if __name__ == "__main__":
    # test
    birthday = Birthday()
    birthday.func_new()
    birthday.func_print_names()
    birthday.func_print_birthday()
    birthday.func_print_birthday("otto")
    birthday.func_print_birthday("")
