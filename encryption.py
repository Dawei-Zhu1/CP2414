"""
CP2414 - Task 4

- Generate the salt (random.uniform)
- Implement a one-way hash function with hashlib

By Zhu Dawei
"""
import random
import hashlib
import rsa


private_key ,public_key = rsa.newkeys(16)
print(private_key, public_key)


def to_encrypt_rsa(raw_string: str, public_key):
    """To have the string encrypted with RSA

    Args:
        raw_string (str): An original string

    Returns:
        tuple: cipher text, public key, and private key
    """

    cipher_string = rsa.encrypt(raw_string.encode(), public_key)
    return cipher_string



def to_encrypt(raw_string, salt):
    """
    To get a string encrypted with the sha256 and salt.
    :param raw_string:
    :param salt:
    :return:
    """    
    # salt = produce_salt(0, 1)
    string_hashed = hashlib.sha256(raw_string.encode('UTF-8'))
    # Add salt
    # According to python handbook, (string_hashed.update) == (string_hashed(raw_string + salt))
    string_hashed.update(str(salt).encode())
    return string_hashed.hexdigest()


def produce_salt(a, b):

    """
    Generate a random salt.
    :param a:
    :param b:
    :return:
    """
    return random.uniform(a, b)


def main():
    """Demonstration of the module."""
    raw_string = 'Hello'
    print('raw_string1:', raw_string)

    string_hashed1 = hashlib.sha256(raw_string.encode())
    raw_string2 = 'Hello'
    print('raw_string2:', raw_string2)
    string_hashed2 = hashlib.sha256(raw_string2.encode('UTF-8'))
    print('string_hashed1:', string_hashed1.hexdigest())
    print('string_hashed2:', string_hashed2.hexdigest())
    print('Is string1 == string2?', string_hashed1.hexdigest() == string_hashed2.hexdigest())
    print('=' * 36)
    salt = produce_salt(0, 1)
    string_encrypted = to_encrypt(raw_string, salt)
    string_hashed_encrypted = to_encrypt(raw_string, salt)
    print(f'salt: {salt}')
    print('string_hashed1:', string_hashed1.hexdigest())
    print('string_encrypted:', string_encrypted)
    print('Is raw_string1 == string_encrypted?', string_hashed1.hexdigest() == string_hashed_encrypted)

    print('\n=== RSA ===')



if __name__ == '__main__':
    main()
