"""
CP2414 - W03 Task2

- Read inputs from keyboard typing
- Check a string’s length and whether contains

    * upper case,
    * lower case,
    * number,
    * and symbol

By Zhu Dawei
"""
import string
import re

MINIMUM_LENGTH = 8
MAXIMUM_LENGTH = 20
SPECIAL_CHARS = string.punctuation.strip()
LEAST_UPPERCASE_NUMBER = 1
LEAST_LOWERCASE_NUMBER = 1
LEAST_DIGIT_NUMBER = 5
LEAST_SPECIAL_CHAR_NUMBER = 1


def get_valid_input(prompt: str = 'Enter: ') -> str:
    """
    To avoid empty string from being input
    """
    user_input = input(prompt).strip()
    # Loop until the input is not empty or with all blank characters
    while not user_input:
        print("Invalid input. Please try again.")
        user_input = input(prompt).strip()
    return user_input


def is_valid_password(password: str) -> bool:
    """
    Determine whether the provided password is valid.
    Returns True if the password is valid.
    Else returns False and display message.
    """

    is_good_length:bool = (MINIMUM_LENGTH <= len(password) <= MAXIMUM_LENGTH)
    # re.findall(r'[A-Z]', password) returns a list of objects that are in uppercase
    is_with_uppercase:bool = (len(re.findall(r'[A-Z]', password)) >= LEAST_UPPERCASE_NUMBER)
    # re.findall(r'[a-z]', password) returns a list of objects that are in lowercase
    is_with_lowercase:bool = (len((re.findall(r'[a-z]', password))) >= LEAST_LOWERCASE_NUMBER)
    # re.findall(r'[0-9]', password) returns a list of objects that are digits
    is_with_digit:bool = (len(re.findall(r'[0-9]', password)) >= LEAST_DIGIT_NUMBER)
    # re.findall(f'[{SPECIAL_CHARS}]', password) returns a list of objects that are with special characters
    is_with_special_chars:bool = (len(re.findall(f'[{SPECIAL_CHARS}]', password)) >= LEAST_SPECIAL_CHAR_NUMBER)
    # Give feedback of a bad password
    if not (is_good_length and is_with_uppercase and is_with_lowercase and is_with_digit and is_with_special_chars):
        error_textlines = []
        # Check length
        if len(password) < MINIMUM_LENGTH:
            error_textlines.append(f'Short! Least {MINIMUM_LENGTH} chars short.')
        elif len(password) > MAXIMUM_LENGTH:
            error_textlines.append(f'Toooooooo loooooong! Password must be at most {MAXIMUM_LENGTH} characters long.')
        # Check other conditions
        if not is_with_uppercase:
            error_textlines.append(f'- Require at least {LEAST_UPPERCASE_NUMBER} UPPERCASE LETTER')
        if not is_with_lowercase:
            error_textlines.append(f'- Require at least {LEAST_LOWERCASE_NUMBER} lowercase letter')
        if not is_with_digit:
            error_textlines.append(f'- Require at least {LEAST_DIGIT_NUMBER} d1git')
        if not is_with_special_chars:
            error_textlines.append(f'- Require at least {LEAST_SPECIAL_CHAR_NUMBER} $pec!al ch@racter')
        # Show error messages
        error_text = '\n'.join(error_textlines)
        print(error_text)
        return False
    return True


def get_valid_password() -> str:
    """To get a valid input from the user for password"""
    raw_password = get_valid_input('Enter your password: \n')
    while not is_valid_password(raw_password):
        raw_password = get_valid_input('Enter your password: \n')
    print('Your password is valid.')
    return raw_password


def main():
    """Demonstration of the module."""
    a = get_valid_input()
    print('You\'ve entered: ', a)


if __name__ == '__main__':
    main()
