"""
CP2414 - Task 4

- Generate the salt (random.uniform)
- Implement a one-way hash function with hashlib

By Zhu Dawei
"""
import random
import math
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad
from input_checking import MAXIMUM_LENGTH


def encrypt_password(data: str, key: bytes) -> bytes:
    """
    To get a string encrypted with the sha256 and salt.
    :param data: Password to encrypt.
    :param key: Salt.
    :return: The encrypted password.
    """
    cipher = DES.new(key, DES.MODE_ECB)
    cipher_size = set_block_size(MAXIMUM_LENGTH)
    cipher_text = cipher.encrypt(pad(data.encode('utf-8'), 24))
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
    cipher = DES.new(key, DES.MODE_ECB)
    cipher_text = encrypt_password(text, key)
    print(cipher_text)
    decrypted = unpad(
        cipher.decrypt(cipher_text),
        set_block_size(MAXIMUM_LENGTH)
    )
    print(decrypted, DES.block_size * 3)


if __name__ == '__main__':
    main()
