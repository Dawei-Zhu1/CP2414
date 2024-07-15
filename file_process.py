"""
CP2414 - W03 Task 3

- Write a string into a file

By Zhu Dawei
"""
import json

DIRECTORY = 'USER_PASSWORD'
FILENAME = 'task3.txt'


def read_user_database(directory: str) -> dict:
    """
    Read the user database file
    :return:
    """
    # Try-except is an error handling mechanism
    # In this case it is used to prevent opening a file that does not exist
    try:
        with open(directory, 'r') as f:
            user_database = json.load(f)
        print('User database loaded.')
    except FileNotFoundError:
        print(f'Warning: The file {directory} does not exist.')
        user_database = dict()
    return user_database


def save_user_database(directory: str, user_database: dict) -> None:
    """
    Save the user database file
    :param directory:
    :param user_database:
    :return: None
    """
    # Error handler if the file is not saved
    try:
        with open(directory, 'w') as f:
            json.dump(user_database, f)
        print('User database has been saved successfully.')
    except IOError:  # If an Input / Output error occurs
        print('Unable to save the user database.')


def save_password_to_file(directory: str, password: str or bytes) -> None:
    """
    Save password to file in byte.
    """
    with open(directory, 'wb') as f:
        f.write(password)


def read_password_from_file(directory: str) -> str or bytes:
    """
    Read password from file in byte.
    """
    with open(directory, 'rb') as f:
        return f.read()


def main():
    """Demonstration of the module."""
    # save_user_database(FILENAME, dict())
    # print(a.decode('ascii'))
    directory = '/'.join((DIRECTORY, FILENAME))
    with open(directory, 'wb') as f:
        f.write(b'M9n\x1dzD\xe1\x02\x91\xe8#x\xcf\xcf\xa5\x97\x91\xe8#x\xcf\xcf\xa5\x97')

    with open(directory, 'rb') as f:
        line = f.readline()
        print(line.__repr__(), type(line))


if __name__ == '__main__':
    main()
