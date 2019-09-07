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
