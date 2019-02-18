import unittest # Importing the unittest module
from credentials import Credentials # Importing the contact class
class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("facebook","miahmamie") # create credential object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.app_name,"tumblr")
        self.assertEqual(self.new_credential.password,"Andersonne")
    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credentials list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credentials.credentials_list),1) 
    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential
        objects to our credentials_list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("tumblr","Andersonne") # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),2)
    #setup and class creation up here
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

# other test cases here
    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential
        objects to our credentials_list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("tumblr","Andersonne") # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),2)
    # More tests above
    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credentials list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("tumblr","Andersonne") # new credential
        test_credential.save_credential()

        self.new_credential.delete_credential()# Deleting a credential  object
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credential_by_app_name(self):
        '''
        test to check if we can find a credential by app_name and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credentials("tumblr","Andersonne") # new credential
        test_credential.save_credential()

        found_credential = Credentials.find_by_app_name("tumblr")

        self.assertEqual(found_credential.app_name,test_credential.app_name)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credentials("tumblr","Andersonne") # new credential
        test_credential.save_credential()

        credential_exists = Credentials.credential_exist("tumblr")

        self.assertFalse(credential_exists)
    def test_display_all_credential(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credential(),Credentials.credentials_list)
if __name__ == '__main__':
    unittest.main()