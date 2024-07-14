"""
CP2414 - Task 4

- Generate the salt (random.uniform)
- Implement a one-way hash function with hashlib

By Zhu Dawei
"""
import random
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad


def encrypt_password(data: str, salt: bytes) -> object:
    """
    To get a string encrypted with the sha256 and salt.
    :param key:
    :param salt:
    :return:
    """
    cipher = DES.new(salt, DES.MODE_ECB)
    cipher_pad = cipher.encrypt(data.encode('utf-8'))
    return cipher


def generate_salt(a, b):
    """
    Generate a random salt.
    :param a:
    :param b:
    :return:
    """
    return random.uniform(a, b)


def main():
    text = '12345678'
    salt = b'12345678'
    cipher = encrypt_password(text, salt)
    print(cipher)


if __name__ == '__main__':
    main()
