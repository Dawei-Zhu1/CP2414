"""
CP2414 - W03 Task 1

- Generate a string, whose length is in [8, 20], containing at least one upper
- case, one lower case, one number and one symbol.
- Then print string
By Zhu Dawei
"""
import random
import string

# Set the string length limits as constants, with which you can adjust them easily
MINIMUM_LENGTH = 8
MAXIMUM_LENGTH = 20
# Use strip() method of string to remove surrounding blank characters (e.g. returns, spaces, tabs)
# string.printable contains blank chars.
# In PyCharm or Visual Studio Code, you can Hold ctrl and click on it to view them.
USABLE_CHARS = string.printable.strip()


def generate_valid_password() -> str:
    """
    Generate a random string until it meets requirements to be a password.
    :return:
    """
    _password = generate_random_string()
    while not is_valid_password(_password):
        # Re-generate random text
        _password = generate_random_string()
    return _password


def generate_random_string() -> str:
    # The type name str in the function declaration part is used to indicate
    # that this function will have a string as return value
    """
    Generate a random string of at least one uppercase, one lowercase, one number and special chars
    :return str: A random string.
    """
    # Generate length of a random integer between the constants of string length limit
    length = random.randint(MINIMUM_LENGTH, MAXIMUM_LENGTH)
    text = ''  # Initialize an empty string
    for i in range(length):
        text += generate_a_character()  # Append the random character to local variable: text
        # text = text + generate_a_character()  # They are equivalent
    return text


def generate_a_character() -> str:
    """
    Generate a random character.
    :return: a character.
    """
    # Use random choice to randomly select one character from the given string/sequence
    return random.choice(USABLE_CHARS)


def is_valid_password(password: str) -> bool:
    """Determine whether the provided password is valid."""
    # Counters record the amount of certain characters
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    # Count the upper, lower, digit, specials
    for char in password:
        # Count special characters
        if char in string.punctuation:
            # (count_special += 1) is equivalent to (count_special = count_special + 1)
            count_special += 1
        # Check whether the password has any lowercase letters
        count_lower += char.islower()
        # Check whether the password has any uppercase letters
        count_upper += char.isupper()
        # Check whether the password has any numbers
        count_digit += char.isdigit()
    # Return True if all requirements are fulfilled, which indicates the given password is valid
    # If one of them is 0 (lack of one of them), then return False
    # In python, 0, empty string '', empty list, none, etc. can be turned in to False
    return bool(count_lower and count_upper and count_digit and count_special)


def repeat_main(number: int) -> None:
    """
    This is a function that repeats the main function of the program for testing purposes
    :param number:
    :return: None
    """
    for i in range(number):
        main()


def main():
    """Demonstration of the module."""
    # help(string)  # Run this to see what is in the string module
    password = generate_valid_password()
    print(password)


if __name__ == '__main__':  # This part will not be executed when it runs as a module
    main()
    # repeat_main(20)
