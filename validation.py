"""
CP2414 - W03 Task5

- Read a string (password) from the keyboard input
- Call your hash function to verify the password

By Zhu Dawei
"""
from password_generator import generate_random_string
from encryption import *


def decrypt_password(raw_string, key, cipher_text):
    """
    To get a string encrypted with the sha256 and salt.
    :param raw_string: Encrypted password
    :param key: salt
    :param cipher_text: Encrypted password in database
    :return:
    """
    cipher = DES.new(key, DES.MODE_ECB)
    _block_size = len(raw_string)
    decrypted_password = cipher.decrypt(raw_string)
    return unpad(decrypted_password, _block_size)


def main():
    """Demonstration of the module."""
    password_for_test = 'Hello'


if __name__ == '__main__':
    main()
