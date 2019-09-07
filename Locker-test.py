from Locker import  Account
from Locker import Credentials
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

    #*******************************************************# credentials
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    Args:
     unittest.TestCase: helps in creating test cases
    '''
    def test_check_user_account(self):
        '''
        Function to test whether the login in function check_user works as expected
        '''
        self.new_user = Account('Umuhire','Anuarithe','111')
        self.new_user.save_user_account()
        user2 = Account('Tuyishime', 'J.Baptiste', 'mwo')
        user2.save_user_account()
        user3 = Account('Tubane', 'Elie', 'Elly')
        user3.save_user_account()

        for user in Account.users_list:
            if user.username == user2.username and user.password == user2.password:
                current_user = user.username
        return current_user
        self.assertEqual(current_user, Credentials.check_user_account(user2.password, user2.username))


if __name__ == '__main__':
    unittest.main()