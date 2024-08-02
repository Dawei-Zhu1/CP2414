import hmac
import base64
from hashlib import sha1


def make_digest(message, key):
    key = bytes(key, 'UTF-8')
    message = bytes(message, 'UTF-8')

    digester = hmac.new(key, message, sha1)
    print(digester)
    # signature1 = digester.hexdigest()
    signature1 = digester.digest()
    # print(signature1)

    # signature2 = base64.urlsafe_b64encode(bytes(signature1, 'UTF-8'))
    signature2 = base64.urlsafe_b64encode(signature1)
    # print(signature2)

    return str(signature2, 'UTF-8')


def main():
    result = make_digest('message', 'private-key')
    print(result)


if __name__ == '__main__':
    main()
