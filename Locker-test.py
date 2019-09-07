from Locker import  Account

import unittest

class TestAccout(unittest.TestCase):
    '''
    Test class that defines test cases for the accout class behaviours.
    Args:
    unittest.TestCase: helps in creating test cases
    '''


    def setUp(self):
        '''
        Function to create a user account before each test
        '''
        self.new_user = Account('Umuhire','Anuarithe','111')


    def test__init__(self):
        '''
        Test to if check the initialization/creation of accounnt   instances is properly done
        '''
        self.assertEqual(self.new_user.fullname, 'Umuhire')
        self.assertEqual(self.new_user.username, 'Anuarithe')
        self.assertEqual(self.new_user.password, '111')

    
    def test_save_user_account(self):
        '''
        Test to check if the new user account info is saved into the users list
        '''
        self.new_user.save_user_account()
        self.assertEqual(len(Account.users_list), 1)


if __name__ == '__main__':
    unittest.main()