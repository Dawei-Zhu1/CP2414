"""
CP2414 - Task 4

- Generate the salt (random.uniform)
- Implement a one-way hash function with hashlib

By Zhu Dawei

Use DES then transform to hex.
"""
import random
import math
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from input_checking import MAXIMUM_LENGTH


def encrypt_password(data: str, key: bytes or str, block_size: int = MAXIMUM_LENGTH) -> str:
    """
    To get a string encrypted with the sha256 and salt.
    :param data: Password to encrypt.
    :param key: Salt.
    :param block_size: Block size, multiple 8s.
    :return: The encrypted password in hex.
    """
    _key = bytes(key.encode('utf-8')) if type(key) is str else key
    cipher = DES.new(_key, DES.MODE_ECB)
    cipher_size = set_block_size(MAXIMUM_LENGTH)
    cipher_text = cipher.encrypt(
        pad(
            data.encode('utf-8'),
            cipher_size
        )
    )
    return cipher_text.hex()


def generate_salt(a, b):
    """
    Generate a random salt.
    :param a: Salt minimum.
    :param b: Salt maximum.
    :return:
    """
    return random.uniform(a, b)


def set_block_size(password_length: int) -> int:
    """
    Set block size with password length.
    """
    return math.ceil(password_length / 8) * DES.block_size


def validate_password(raw_string: str, key: str or bytes, stored_password: str) -> bool:
    """
    To get a string encrypted with the sha256 and salt.
    :param raw_string: Encrypted password
    :param key: salt
    :param stored_password: Encrypted password in database
    :return: Comparison between encrypted password and stored password
    """
    password_to_be_verified = raw_string
    _stored_password = stored_password
    _key = key
    # Encrypt the raw string
    _block_size = len(raw_string)
    cipher_text_to_be_verified = encrypt_password(password_to_be_verified, key)
    return cipher_text_to_be_verified == _stored_password


def main():
    key = b'12345678'
    text = 'Helloooo'
    cipher_text = encrypt_password(text, key)
    print(cipher_text, len(cipher_text))


if __name__ == '__main__':
    main()
