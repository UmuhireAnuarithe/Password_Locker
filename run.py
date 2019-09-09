#! /usr/bin/env python3
from Locker import Account
from Locker import Credentials
import pyperclip
import  random

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

def generate_password(credential):
    '''
    Function to generate a password automatically
    '''
    password_generate= credential.generate_password()
    return password_generate


def create_credential(user_name, site_name, account_name, password):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(user_name, site_name, account_name, password)

    return new_credential


def save_credential(credential):
    '''
    Function to save a newly created credential
    '''

    Credentials.save_credentials(credential)


def display_credentials(user_name):
    '''
    Function to display credentials saved by a user
    '''
    return Credentials.display_credentials(user_name)

def copy_credential(site_name):
    '''
    Function to copy a credentials details to the clipboard
    '''
    return Credentials.copy_credential(site_name)

def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    return credential.delete_credential()



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
            print("-"*40)
            print(' ')
            print('To login, enter your account details:')
            username = input('Enter your user name - ')
            password = str(input('Enter your password - '))
            user_exists = confirm_user(username, password)
            if user_exists == username:
                print(" ")
                print(f'Welcome {fullname}. Please choose an option to continue.')
                # print(' ')

                print(' ')
                while True:

                    print("-"*30)
                    print(
                        'Use short-codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n del-delete credential \n ex-Exit')
                    short_code = input('Enter a choice: ').lower().strip()
                    print("-"*30)
                    if short_code == 'ex':
                        print(" ")
                        print(f'Goodbye {fullname}')
                        break
                    elif short_code == 'cc':
                        print(' ')
                        print('Enter your credential details:')
                        print("-"*30)
                        print(" Enter user name")
                        user_name = input()
                        print(" Enter site name ")
                        site_name = input()
                        print("Enter account name")
                        account_name = input()
                        
                        while True:
                            print(' ')
                            print("-"*100)
                            print(
                                'Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
                            psw_choice = input(
                                'Enter an option: ').lower().strip()
                            print("-"*100)
                            if psw_choice == 'ep':
                                print(" ")
                                password = input(
                                    'Enter your password: ').strip()
                                break
                            elif psw_choice == 'gp':
                                # password = generate_password()
                                string="abcdefghijklmnopqrstuvwxyz0123456789"
                                password=''.join(random.choice(string) for _ in range(8))
                                break
                            elif psw_choice == 'ex':
                                break
                            else:
                                print('Oops! Wrong option entered. Try again.')
                        save_credential(create_credential(
                            user_name, site_name, account_name, password))
                        print(' ')
                        print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
                        print(' ')

                    elif short_code == 'dc':
                        print(' ')
                        if display_credentials(user_name):

                            print('Here is a list of all your credentials')
                            print(' ')
                            for credential in display_credentials(user_name):
                                print(
                                    f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
                            print(' ')
                        else:
                            print(' ')
                            print("You don't seem to have any credentials saved yet")
                            print(' ')
                             

                    
                    elif short_code == 'copy':
                        print(' ')
                        chosen_site = input('Enter the site name for the credential password to copy: ')
                        copy_credential(chosen_site)
                        print('')
                    # else:
                    #     print('Try again.')

                    elif short_code == 'del':
                        # session_header(u_name)
                        print("       Delete Credential")
                        print("     "+"="*20)
                        print ('\n')

                        site_name = input("Enter site Name:")
                        # found_credential = find_by_site_name( site_name)
                        # if found_credential:
                        #     print(f"Here are the credentials for {found_credential.(credential.site_name)}:")
                        found_credential = Credentials.find_by_site_name(credential.site_name)
                        print(f"User Account: {found_credential.credential_user_name}")
                        print(f"Password: {found_credential.credential_password}")
                        if input("\033[1;31;40m Are you sure you want to delete it? (Y/N) \033[0;0m ").upper() == "Y":
                         delete_credential(found_credential)
                        print()
                        print("Press Enter to continue")
                        input(f" \033[1;32;40m Credentials for {found_credential.credential_site} deleted. \033[0;0m ")
                    else:
                            print(f" \033[1;31;40m Credentials Not Found for {site_name}! \033[0;0m ")
                            print("Press Enter to continue")
                            input()
if __name__ == '__main__':
    main()