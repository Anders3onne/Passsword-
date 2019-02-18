
class user:
    """
    Class that generates new instances of users.
    """

    user_list = [] # Empty user list

 # Init method up here

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        user.user_list.append(self)



    def __init__(self,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        user.user_list.remove(self)


    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = user("Test","user","07865728262","test@user.com") # new usert
        test_user.save_user()

        user_exists = user.user_exist("0711223344")

        self.assertTrue(user_exists)
         
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list