"""
CP2414 - Task 4

- Generate the salt (random.uniform)
- Implement a one-way hash function with hashlib

By Zhu Dawei

Use rsa then transform byte to hex.
"""
import typing

import rsa


def generate_keys(a: int) -> (rsa.PrivateKey, rsa.PublicKey):
    """
    Generate a random salt.
    :param a: length of key
    :return:
    """
    return rsa.newkeys(a)


def encrypt_password(message: any, key: rsa.PublicKey) -> str:
    """
    To get a string encrypted with the sha256 and salt.
    :param message: Password to encrypt.
    :param key: rsa key.
    :return: The encrypted password in hex.
    """

    _key = key
    _message = bytes(message.encode())
    cipher_text = rsa.encrypt(_message, _key)
    return cipher_text.hex()


def export_key(key: rsa.key) -> any:
    """
    Transform a rsa private key into a string.
    """
    _key = key
    return _key.save_pkcs1().decode()


def import_key(key_string: str) -> any:
    """
    Import a rsa private key string.
    """
    _key = bytes(key_string.encode())
    if b'PRIVATE KEY' in _key:
        return rsa.PrivateKey.load_pkcs1(_key)
    elif b'PUBLIC KEY' in _key:
        return rsa.PublicKey.load_pkcs1(_key)
    else:
        raise ValueError(f'Invalid key string')


def validate_password(raw_string: str, key: str, stored_password: str) -> bool:
    """
    To get a string encrypted with rsa.
    When using rsa, same message will have different ciphers even with the same public key.
    :param raw_string: Encrypted password
    :param key: Private key.
    :param stored_password: Encrypted password in database
    :return: Comparison between encrypted password and stored password
    """
    password_to_be_verified = raw_string
    _stored_password = bytes.fromhex(stored_password)
    _key = import_key(key)
    cipher_text_to_be_verified = rsa.decrypt(_stored_password, _key).decode()
    return cipher_text_to_be_verified == password_to_be_verified


def main():
    key_public, key_private = rsa.newkeys(512)
    text = 'Hellooo0'
    cipher1 = encrypt_password(text, key_public)
    print(rsa.decrypt(bytes.fromhex(cipher1), key_private))
    print(validate_password(text, key_private.save_pkcs1().decode(), cipher1))


if __name__ == '__main__':
    main()
