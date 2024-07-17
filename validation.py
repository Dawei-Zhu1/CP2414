"""
CP2414 - W03 Task5

- Read a string (password) from the keyboard input
- Call your hash function to verify the password

By Zhu Dawei
"""
from encryption import *


def validate_password(raw_string, key, cipher_text):
    """
    To get a string encrypted with the sha256 and salt.
    :param raw_string: Encrypted password
    :param key: salt
    :param cipher_text: Encrypted password in database
    :return:
    """
    password_to_be_verified = raw_string
    stored_password = cipher_text
    _key = key
    cipher = DES.new(_key, DES.MODE_ECB)
    _block_size = len(raw_string)
    decrypted_password = cipher.decrypt(raw_string)
    return unpad(decrypted_password, _block_size)


def main():
    """Demonstration of the module."""
    password_for_test = 'Hello'


if __name__ == '__main__':
    main()
