"""
This python program is a collection of previous tasks to build a password manage system.
By Zhu Dawei
"""
import os.path
import shutil

from password_generator import generate_valid_password, generate_random_string
from input_checking import get_valid_input, get_valid_password
from file_process import read_user_database, save_user_database, save_password_to_file
from encryption import *

import facial_recognition

FACES_DIRECTORY = 'data/faces'
USER_DATABASE_DIRECTORY = 'user_password_database.json'
RSA_KEY_LENGTH = 1536

# Code to input
CHOICE_QUIT = '0'
CHOICE_REGISTER = '1'
CHOICE_LOGIN = '2'
CHOICE_CHECK_ACCOUNTS = '3'


def show_menu() -> None:
    """
    To display the menu
    """
    print('1. Register')
    print('2. Login')
    print('3. Show Accounts')
    print('0. Quit')


class PasswordManagement:
    def __init__(self):
        self.password_database = read_user_database(USER_DATABASE_DIRECTORY)
        pass

    def main(self) -> None:
        print('Welcome!')
        show_menu()
        choice = get_valid_input('Type your option number: ')
        while choice is not CHOICE_QUIT:
            if choice is CHOICE_REGISTER:
                self.register()
            elif choice is CHOICE_LOGIN:
                self.login()
            elif choice is CHOICE_CHECK_ACCOUNTS:
                self.show_accounts()
            else:
                print('Invalid option. Please try again.')
            # Loop restarts here
            choice = get_valid_input('Type your option number: ')

    def register(self) -> None:
        """
        Register a new user
        """
        # Set username
        username = get_valid_input('Enter your username: ')
        print(f'Hello {username}')

        # Password - setting / suggestion
        courtesy_password = generate_valid_password()  # Password of suggestion
        print(f'Our suggestion for your password:\n{courtesy_password}')
        accept_suggestion = input('Do you want to use this password? (Y/n) ')
        if accept_suggestion.upper() == 'Y':  # If user wants to use the courtesy password
            raw_password = courtesy_password
        else:  # Else set password by themselves
            raw_password = get_valid_password()
        # Ask for photo
        photo_directory = facial_recognition.input_photo()
        photo_extension = os.path.splitext(photo_directory)[1]
        shutil.copy2(photo_directory, os.path.join(FACES_DIRECTORY, username + photo_extension))

        # Encryption
        public_key, private_key = generate_keys(RSA_KEY_LENGTH)
        # Hash Password
        salt = generate_random_string()
        hashed_password = hash_password(raw_password, salt)
        encrypted_password = encrypt_password(message=hashed_password, key=public_key)
        public_key_to_save = export_key(public_key)
        private_key_to_save = export_key(private_key)
        self.password_database[username] = {
            'public_key': public_key_to_save,
            'private_key': private_key_to_save,
            'salt': salt,
            'password': encrypted_password
        }  # Put this record into database

        # Save the database
        save_user_database(USER_DATABASE_DIRECTORY, self.password_database)
        print(f'Thank you, {username}! Your account has been added to database successfully.')

    def login(self) -> None:
        """
        User login procedure.
        """
        # Ask user to input username and password
        username = get_valid_input('Enter your username: ')
        entered_password = get_valid_input('Enter your password: ')
        # Check whether the username exists in database records
        if username in self.password_database:
            # Get salt from record then encrypt the entered password
            record = self.password_database[username]
            program = facial_recognition.FacialRecognition(FACES_DIRECTORY)
            if validate_password(
                    raw_string=entered_password,
                    salt=record['salt'],
                    key=record['private_key'],
                    stored_password=record['password']
            ) and program.recognize_face(username):
                print(f'Welcome, {username}')
            else:
                print('Login failed,')
        else:
            print('Your account does not exist.')

    def show_accounts(self) -> None:
        """
        Display all user accounts'
        """
        account_count = len(self.password_database)
        print(f'There are {account_count} accounts available:')
        for username in self.password_database:
            print(username)


def main():
    program = PasswordManagement()
    program.main()


if __name__ == '__main__':
    main()
