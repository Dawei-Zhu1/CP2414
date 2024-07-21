"""
CP2414 - W03 Task 1

- Generate a string, whose length is in [8, 20], containing at least one upper
- case, one lower case, one number and one symbol.
- Then print string
By Zhu Dawei
"""
import random
import string
from input_checking import is_valid_password

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
    while not is_valid_password(_password, print_errors=False)[0]:
        # Re-generate random text
        _password = generate_random_string()
    return _password


def generate_random_string(length: int = 8) -> str:
    # The type name str in the function declaration part is used to indicate
    # that this function will have a string as return value
    """
    Generate a random string of at least one uppercase, one lowercase, one number and special chars
    :return str: A random string.
    """
    # Generate length of a random integer between the constants of string length limit
    _length = length
    text = ''  # Initialize an empty string
    for i in range(_length):
        text += generate_a_character()  # Append the random character to local variable: text
        # text = text + generate_a_character()  # They are equivalent
    return text


def generate_a_character(type: str = '') -> str:
    """
    Generate a random character.
    :return: a character.
    """
    # Use random choice to randomly select one character from the given string/sequence
    if type == 'upper':
        return random.choice(string.ascii_uppercase)
    elif type == 'lower':
        return random.choice(string.ascii_lowercase)
    elif type == 'number':
        return random.choice(string.digits)
    elif type == 'symbol':
        return random.choice(string.punctuation)
    else:
        # Return random
        return random.choice(USABLE_CHARS)


def main():
    """Demonstration of the module."""
    # help(string)  # Run this to see what is in the string module
    password = generate_valid_password()
    print(password)


if __name__ == '__main__':  # This part will not be executed when it runs as a module
    main()
