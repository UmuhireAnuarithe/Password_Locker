from Locker import  Account
from Locker import Credentials
import unittest
import  pyperclip  
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
    

    def setUp(self):
        '''
        Function to create an account's credentials before each test
        '''
        self.new_credential = Credentials(
            'Justine', 'Twitter', 'Mpanoyimana', 'Mpano')

    def test__init__(self):
        '''
        Test to if check the initialization of credential instances is properly done
        '''
        self.assertEqual(self.new_credential.user_name, 'Justine')
        self.assertEqual(self.new_credential.site_name, 'Twitter')
        self.assertEqual(self.new_credential.account_name, 'Mpanoyimana')
        self.assertEqual(self.new_credential.password, 'Mpano')



    def test_save_credentials(self):
        '''
        Test to check if the new credential info is saved into the credentials list
        '''
        self.new_credential.save_credentials()
        twitter = Credentials('James', 'Twitter', 'jimmy', '555')
        twitter.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        '''
        Function to clear the credentials list after every test
        '''
        Credentials.credentials_list = []
        Account.users_list = []

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credetial to check if we can save multiple credential 
            objects to our credetial_list
            '''
            self.new_credential.save_credentials()
            One = Credentials('Jacob', 'Instagram', 'jac', '888') # new contact
            One.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)



    def test_display_credentials(self):
        '''
        Test to check if the display_credentials method, displays the correct credentials.
        '''
        self.new_credential.save_credentials()
        Facebook = Credentials('Jay', 'Facebook', 'jade', '777')
        Facebook.save_credentials()
        self.assertEqual(len(Credentials.display_credentials(Facebook.user_name)), 1)

    def test_delete_credential(self):
        '''
        test_delete_cred to test if we can remove a credential from our credentials list
        '''
        self.new_credential.save_credentials()
        test_credenntial = Credentials("David","Twitter", "dave", "ddd") # new credential
        test_credenntial .save_credentials()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_by_site(self):
        '''
        Test to check if the find_by_site_name method returns the correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credentials('James', 'Twitter', 'jimmy', '555')
        twitter.save_credentials()
        credential_exists = Credentials.find_by_site_name('Twitter')
        self.assertEqual(credential_exists, twitter)
    


    def test_copy_credential(self):
        '''
        Test to check if the copy a credential method copies the correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credentials('James', 'Twitter', 'jimmy', '555')
        twitter.save_credentials()
        find_credential = None
        for credential in Credentials.user_credentials_list:
            find_credential = Credentials.find_by_site_name(
                credential.site_name)
            return pyperclip.copy(find_credential.password)
        Credentials.copy_credential(self.new_credential.site_name)
        self.assertEqual('555', pyperclip.paste())
        print(pyperclip.paste())

if __name__ == '__main__':
    unittest.main()