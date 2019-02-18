
class Credentials:

    credentials_list = []  # Empty credentials list

    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)

    def __init__(self, username, pas):
        self.username = "admin"
        self.pas = "admin12"

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)

    def credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = credentials("andy","andy123") # new credentials
        test_credentials.save_credentials()

        Credentials_exists = credentials.credentials_exist("andy")

        self.assertTrue(credentials_exists)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the user list
        '''
        return cls.credentials_list