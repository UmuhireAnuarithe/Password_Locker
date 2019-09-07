#! /usr/bin/env python3
from Locker import Account
from Locker import Credentials


def create_user(fullname, username, password):
    '''
    Function to create a new user account
    '''
    new_user = Account(fullname, username, password)
    new_user.save_user_account()
    return new_user


def save_user_account(user):
    '''
    Function to save a new user account
    '''
    Account.save_user_account(user)

def confirm_user(username, password):
    '''
    Function that verifies the existance of the user before creating credentials
    '''
    cheked_user = Credentials.check_user_account(username, password)

    return cheked_user


def main():
    print(' ')
    print('Hello! Welcome to Password Locker.')
    while True:
        print(' ')
        print("*"*100)
        print(
            'Use these codes to continue: \n ca-Create an Account \n li-Log In \n ex-Exit')
        short_code = input('Enter a option: ').lower().strip()
        if short_code == 'ex':
            break

        elif short_code == 'ca':
            print("*"*50)
            print(' ')
            print('To generate a new account:')
            print("*"*50)
            print("Enter your full name")
            fullname = input()
            print(" Enter your username")
            username = input()
            print("Enter your password")
            password = input()
            save_user_account(create_user(fullname, username, password))
          
            print(f'New Account Created for: {fullname} successfully created')
        elif short_code == 'li':
            print("-"*100)
            print(' ')
            print('To login, enter your account details:')
            username = input('Enter your user name - ')
            password = str(input('Enter your password - '))
            user_exists = confirm_user(username, password)
            if user_exists == username:
                print(" ")

if __name__ == '__main__':
    main()