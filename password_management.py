"""
This python program is a collection of previous tasks to build a password manage system.
By Zhu Dawei
"""
from password_generator import generate_valid_password
from input_checking import get_valid_input, get_valid_password
from file_process import read_user_database, save_user_database
from encryption import encrypt_password, generate_salt
from decryption import verify_password
# Use json module to turn python dictionary into a widely-used data format
import json

# import rsa

USER_DATABASE_DIRECTORY = 'user_database.json'
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


def main():
    # Read from a file with usernames and passwords
    user_database = read_user_database(USER_DATABASE_DIRECTORY)
    print('Welcome!')
    show_menu()
    choice = get_valid_input('Type your option number: ')
    # Loop while user does not choose to quit
    while choice != CHOICE_QUIT:
        if choice == CHOICE_REGISTER:  # When user wants to register
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
            salt = generate_salt(0, 15)
            password = encrypt_password(password_for_checking, salt)
            user_database[username] = [password, salt]  # Put this record into database
            # The record is in the dictionary {username: [password, salt]}
            # Save the database
            save_user_database(USER_DATABASE_DIRECTORY, user_database)
            print(f'Thank you, {username}! Your account has been created successfully.')

        if choice == CHOICE_LOGIN:  # When user wants to log in
            with open(USER_DATABASE_DIRECTORY, 'r') as f:
                user_database = json.load(f)
            # Ask user to input username and password
            username = get_valid_input('Enter your username: ')
            password_for_verification = get_valid_input('Enter your password: ')
            # Check whether the username exists in database records
            if username in user_database:
                record = user_database[username]
                actual_password = record[0]
                salt = record[1]
                decrypted_password = verify_password(password_for_verification, salt)
                if decrypted_password == actual_password:
                    print(f'Welcome, {username}')
                else:
                    print('Login failed,')
            else:
                print('Your account does not exist.')
        elif choice == CHOICE_CHECK_ACCOUNTS:  # Show accounts
            account_count = len(user_database)
            print(f'There are {account_count} accounts available:')
            for username in user_database:
                print(username)
        else:
            print('Invalid option. Please try again.')
        print()  # Print a newline
        # Loop restarts here
        show_menu()
        choice = get_valid_input('Type your option number: ')


if __name__ == '__main__':
    # main()
    help(rsa)
