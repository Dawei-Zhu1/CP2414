"""
This python program is a collection of previous tasks to build a password manage system.
By Zhu Dawei
"""
from password_generator import generate_valid_password, generate_random_string
from input_checking import get_valid_input, get_valid_password
from file_process import read_user_database, save_user_database, save_password_to_file
from encryption import *
# from decryption import decrypt_password
from operator import attrgetter
# Use json module to turn python dictionary into a widely-used data format
import json

# import rsa

USER_DATABASE_DIRECTORY = 'USER_PASSWORD'
USER_PASSWORD_INDEX_NAME = 'user_password.json'
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
        self.user_database = read_user_database('user_database.json')
        pass

    def main(self):
        print('Welcome!')
        show_menu()
        choice = get_valid_input('Type your option number: ')
        while choice is not CHOICE_QUIT:
            if choice is CHOICE_REGISTER:
                self.to_register()
            elif choice is CHOICE_LOGIN:
                self.to_login()
            elif choice is CHOICE_CHECK_ACCOUNTS:
                self.show_accounts()
            else:
                print('Invalid option. Please try again.')
            # Loop restarts here
            choice = get_valid_input('Type your option number: ')

    def to_register(self):
        # Set username
        username = get_valid_input('Enter your username: ')
        courtesy_password = generate_valid_password()  # Password of suggestion
        print(f'Hello {username}')

        # Password - setting / suggestion
        print(f'Our suggestion for your password:\n{courtesy_password}')
        accept_suggestion = input('Do you want to use this password? (Y/n) ')
        if accept_suggestion.upper() == 'Y':  # If user wants to use the courtesy password
            password_for_checking = courtesy_password
        else:  # Else set password by themselves
            password_for_checking = get_valid_password()

        # Encryption
        salt = generate_random_string(8)
        password = encrypt_password(data=password_for_checking, key=salt)
        password_directory = '/'.join([USER_DATABASE_DIRECTORY, f'{username}.pwd'])
        save_password_to_file(password_directory, password)
        with open(password_directory, 'wb+') as f:
            f.write(password)
        self.user_database[username] = {'password': password, 'key': salt}  # Put this record into database
        print(self.user_database)
        # The record is in the dictionary {username: [password, key]}

        # Save the database
        # save_user_database(USER_DATABASE_DIRECTORY, user_database)
        # print(f'Thank you, {username}! Your account has been created successfully.')

    def to_login(self):
        # Ask user to input username and password
        username = get_valid_input('Enter your username: ')
        entered_password = get_valid_input('Enter your password: ')
        # Check whether the username exists in database records
        if username in self.user_database:
            # Get salt from record then encrypt the entered password
            record = self.user_database[username]
            password_to_verify = encrypt_password(entered_password, record['key'])
            if record['password'] == password_to_verify:
                print(f'Welcome, {username}')
            else:
                print('Login failed,')
        else:
            print('Your account does not exist.')

    def show_accounts(self):
        account_count = len(self.user_database)
        print(f'There are {account_count} accounts available:')
        for username in self.user_database:
            print(username)


def main():
    program = PasswordManagement()
    program.main()


if __name__ == '__main__':
    main()
