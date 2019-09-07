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



if __name__ == '__main__':
    unittest.main()