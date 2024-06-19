"""
CP2414 - W03 Task5

- Read a string (password) from the keyboard input
- Call your hash function to verify the password

By Zhu Dawei
"""
import hashlib
from W03_task1 import generate_random_string
from W03_task2 import get_valid_input, is_valid_password
from W03_task4 import to_encrypt
import random


def to_verify(raw_string, salt):
    """
    To get a string encrypted with the sha256 and salt.
    :param raw_string:
    :param salt:
    :return:
    """
    string_hashed = hashlib.sha256(raw_string.encode('UTF-8'))
    # Add salt
    string_hashed.update(str(salt).encode())
    return string_hashed.hexdigest()


def main():
    """Demonstration of the module."""
    password_for_test = 'Hello'
    print('password_for_test:', password_for_test)
    string_hashed = hashlib.sha256(password_for_test.encode('UTF-8'))
    salt = random.uniform(0, 1)
    string_hashed.update(str(salt).encode())
    password = string_hashed.hexdigest()

    text = input('Input this password or try something else: ')
    string_hashed2 = to_verify(text, salt)
    print(string_hashed2 == password)


if __name__ == '__main__':
    main()
