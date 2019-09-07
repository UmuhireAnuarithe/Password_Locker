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
