"""
CP2414 - W03 Task 3

- Write a string into a file

By Zhu Dawei
"""
import json

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


def main():
    """Demonstration of the module."""
    save_user_database(FILENAME, dict())


if __name__ == '__main__':
    main()
