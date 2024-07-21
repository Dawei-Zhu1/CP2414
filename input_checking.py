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


def is_valid_password(
        password: str,
        minimum_length: int = MINIMUM_LENGTH,
        maximum_length: int = MAXIMUM_LENGTH,
        require_uppercase: bool = LEAST_SPECIAL_CHAR_NUMBER,
        require_lowercase: bool = LEAST_LOWERCASE_NUMBER,
        require_special_chars: int = LEAST_SPECIAL_CHAR_NUMBER,
        require_numbers: bool = LEAST_DIGIT_NUMBER,
        print_errors: bool = False
) -> tuple[bool, str]:
    """
    Determine whether the provided password is valid.
    Returns True if the password is valid.
    Else returns False and display message.
    """
    error_messages = []

    is_good_length: bool = (minimum_length <= len(password) <= maximum_length)

    # re.findall(r'[A-Z]', password) returns a list of objects that are in uppercase
    is_with_uppercase: bool = (len(re.findall(r'[A-Z]', password)) >= LEAST_UPPERCASE_NUMBER)

    # re.findall(r'[a-z]', password) returns a list of objects that are in lowercase
    is_with_lowercase: bool = (len((re.findall(r'[a-z]', password))) >= LEAST_LOWERCASE_NUMBER)

    # re.findall(r'[0-9]', password) returns a list of objects that are digits
    is_with_digit: bool = (len(re.findall(r'[0-9]', password)) >= LEAST_DIGIT_NUMBER)

    # re.findall(f'[{SPECIAL_CHARS}]', password) returns a list of objects that are with special characters
    is_with_special_chars: bool = (len(re.findall(f'[{SPECIAL_CHARS}]', password)) >= LEAST_SPECIAL_CHAR_NUMBER)
    # Give feedback of a bad password
    is_valid: bool = (
            is_good_length and is_with_uppercase and is_with_lowercase and is_with_digit and is_with_special_chars
    )

    if not is_valid:
        # Show password length issue

        if not is_good_length:
            if len(password) < MINIMUM_LENGTH:
                error_messages.append(f'Short! Least {minimum_length} chars short.')
            elif len(password) > MAXIMUM_LENGTH:
                error_messages.append(
                    f'Toooooooo loooooong! Password must be at most {maximum_length} characters long.')

        if require_uppercase and not is_with_uppercase:
            error_messages.append(f'- Require at least {require_uppercase} UPPERCASE LETTER')

        if require_lowercase and not is_with_lowercase:
            error_messages.append(f'- Require at least {LEAST_LOWERCASE_NUMBER} lowercase letter')

        if require_numbers and not is_with_digit:
            error_messages.append(f'- Require at least {LEAST_DIGIT_NUMBER} d1git')

        if require_special_chars and not is_with_special_chars:
            error_messages.append(f'- Require at least {LEAST_SPECIAL_CHAR_NUMBER} $pec!al ch@racter')
    return is_valid, '\n'.join(error_messages)


def get_valid_password() -> str:
    """To get a valid input from the user for password"""
    raw_password = get_valid_input('Enter your password: \n')
    while not is_valid_password(raw_password)[0]:
        raw_password = get_valid_input('Enter your password: \n')
    print('Your password is valid.')
    return raw_password


def main():
    """Demonstration of the module."""
    a = get_valid_input()
    print('You\'ve entered: ', a)


if __name__ == '__main__':
    main()
