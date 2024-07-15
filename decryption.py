"""
CP2414 - W03 Task5

- Read a string (password) from the keyboard input
- Call your hash function to verify the password

By Zhu Dawei
"""
import hashlib
from password_generator import generate_random_string
from input_checking import get_valid_input, is_valid_password
from encryption import encrypt_password
import random


def decrypt_password(raw_string, salt):
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


if __name__ == '__main__':
    main()
