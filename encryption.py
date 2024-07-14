"""
CP2414 - Task 4

- Generate the salt (random.uniform)
- Implement a one-way hash function with hashlib

By Zhu Dawei
"""

# Printable character Info - Google Ascii Code for reference
PRINTABLE_CODE_BEGIN = 33
PRINTABLE_CODE_END = 126
CHARACTER_QUANTITY = 95


def encrypt_password(raw_string, offset):
    """
    To get a string encrypted with the sha256 and salt.
    :param raw_string:
    :param offset:
    :return:
    """
    _text = raw_string
    _offset = offset
    result = ''
    for char in _text:
        # Encrypt uppercase characters in plain text
        result += chr((ord(char) + _offset - PRINTABLE_CODE_BEGIN) % CHARACTER_QUANTITY + PRINTABLE_CODE_BEGIN)
    return result


def main():
    text = 'aaaaaa'
    offset = 1
    encrypted_text = encrypt_password(text, offset)
    print(f'original: {text}\noffset: {offset}\ndecrypted: {encrypted_text}')
    print('Now decrypt')
    decrypted_text = encrypt_password(encrypted_text, -offset)
    print(decrypted_text)
    assert text == decrypted_text


if __name__ == '__main__':
    main()
