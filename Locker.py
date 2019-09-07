import random
import string


class Account:
    # class variable
    users_list = []

    def __init__(self, fullname, username, password):
        '''
        Method to define the properties for each user object will hold.
        '''

        # instance variables

        self.fullname = fullname
        self.username = username
        self.password = password

    def save_user_account(self):
        '''
        Function to save a newly created account instance
        '''
        Account.users_list.append(self)

    #**********************************************# Credentiaals
class Credentials :
    '''
    Class to create  account credentials, generate passwords and save their information
    '''
    # Class Variables
    credentials_list = []
    user_credentials_list = []

    @classmethod
    def check_user_account(cls, username, password):
        '''
        Method that checks if the name and password entered match entries in the users_list
        '''
        current_user = ''
        for user in Account.users_list:
            if (user.username == username and user.password == password):
                current_user = user.username

                return current_user
    

    def __init__(self, user_name, site_name, account_name, password):
            '''
            Method to define the properties for each user object will hold.
            '''

            # ***** instance variables *****#

            self.user_name = user_name
            self.site_name = site_name
            self.account_name = account_name
            self.password = password
    
    def generate_password(self,size=6, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
            '''
            Function to generate an 6 character password for a credential
            '''
            password_generated = ''.join(random.choice(char)
                                        for _ in range(size))
            return password_generated


    def save_credentials(self):
            '''
            Function to save a newly created usercredetials instance
            '''
            
            Credentials.credentials_list.append(self)

    @classmethod
    def display_credentials(cls, user_name):
            '''
            Class method to display the list of credentials saved
            '''
            user_credentials_list = []
            for credential in cls.credentials_list:
                if credential.user_name == user_name:
                    user_credentials_list.append(credential)
            return user_credentials_list
    @classmethod
    def find_by_site_name(cls, site_name):
            '''
            Method that takes in a site_name and returns a credential that matches that site_name.
            '''
            for credential in cls.credentials_list:
                if credential.site_name == site_name:
                    return credential