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
