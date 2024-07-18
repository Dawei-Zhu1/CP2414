"""
CP2414 - Task 4

- Generate the salt (random.uniform)
- Implement a one-way hash function with hashlib

By Zhu Dawei

Use rsa then transform byte to hex.
"""
import rsa


def generate_keys(a: int) -> (rsa.PrivateKey, rsa.PublicKey):
    """
    Generate a random salt.
    :param a: length of key
    :return:
    """
    return rsa.newkeys(a)


def encrypt_password(data: any, key: rsa.PublicKey) -> str:
    """
    To get a string encrypted with the sha256 and salt.
    :param data: Password to encrypt.
    :param key: rsa key.
    :return: The encrypted password in hex.
    """

    _key = key
    cipher_text = rsa.encrypt(data, _key)
    return cipher_text.hex()


def export_key(key: rsa.PrivateKey) -> str:
    """
    Transform a rsa private key into a string.
    """
    return key.save_pkcs1().decode()


def import_key(key_string: str) -> any:
    """
    Import a rsa private key string.
    """
    _key = bytes(key_string.encode())
    if b'PRIVATE KEY' in _key:
        return rsa.PrivateKey.load_pkcs1(_key)
    elif b'PUBLIC KEY' in _key:
        return rsa.PublicKey.load_pkcs1(_key)


def validate_password(raw_string: str, key: str, stored_password: str) -> bool:
    """
    To get a string encrypted with the sha256 and salt.
    :param raw_string: Encrypted password
    :param key: salt
    :param stored_password: Encrypted password in database
    :return: Comparison between encrypted password and stored password
    """
    password_to_be_verified = raw_string
    _stored_password = stored_password
    _key = rsa.PrivateKey.load_pkcs1(bytes(key))
    # Encrypt the raw string
    cipher_text_to_be_verified = encrypt_password(password_to_be_verified, key)
    return cipher_text_to_be_verified == _stored_password


def main():
    key_public, key_private = rsa.newkeys(1024)
    text = b'Hellooo'
    cipher = encrypt_password(text, key_public)
    print(cipher)
    a = export_key(key_private)
    print(a)
    print(import_key(a))


if __name__ == '__main__':
    main()
