class Account:

    users_list = []

    def __init__(self, fullname, username, password):
        '''
        Method to define the properties for each user object will hold.
        '''

        # instance variables

        self.fullname = fullname
        self.username = username
        self.password = password
