"""
CP2414 - Task 4

- Generate the salt (random.uniform)
- Implement a one-way hash function with hashlib

By Zhu Dawei
"""
import random
import math
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from input_checking import MAXIMUM_LENGTH
from decryption import *


def encrypt_password(data: str, key: bytes or str, block_size: int = MAXIMUM_LENGTH) -> bytes:
    """
    To get a string encrypted with the sha256 and salt.
    :param data: Password to encrypt.
    :param key: Salt.
    :param block_size: Block size, multiple 8s.
    :return: The encrypted password.
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
    return cipher_text


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


def main():
    key = b'12345678'
    text = 'Helloooo'
    cipher_text = encrypt_password(text, key)
    print(cipher_text, len(cipher_text))
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted = decrypt_password(cipher_text, key)
    print(decrypted, DES.block_size * 3)


if __name__ == '__main__':
    main()
