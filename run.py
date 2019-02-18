

from user import user
from credentials import Credentials


def login_credentials(xusername, xpassword):
    '''
    Function to create login credentials
    '''
    new_credentials = credentials(xusername, xpassword)
    return new_credentials


def save_credentials(credentials):
    credentials.save_credentials()


def del_credentials(credentials):
    '''
    Function to delete a user
    '''
    credentials.delete_credentials()


def create_user(fname, lname, phone, email):
    '''
    Function to create a new user
    '''
    new_user = user(fname, lname, phone, email)
    return new_user


def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()


def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return user.find_by_number(number)


def check_existing_users(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return user.user_exist(number)


def check_existing_credentials():
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return Credentials.credentials_exist()


def display_users():
    '''
    Function that returns all the saved users
    '''
    return user.display_users()


def display_credentials():
    '''
    Function that returns all the saved users
    '''
    return Credentials.display_credentials()


def main():
    print("Hello Welcome to your user list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : bc - create username and password cc - Personal details, dc - display users,zc - Here is a list of all your login credentials, ac-delete credentials, ex -exit the user list ")

        short_code = input().lower()

        if short_code == 'bc':
            print("New user enter  your login credentials")
            print("-"*10)

            print(" Username ...")
            xusername = input()

            print(" Do you want a generated password?")
            short_code = input().lower()
            if short_code == "yes":
                xpassword = "andy1234"
                print(" Your generated password is andy1234 ")
            else:
                print("Password ...")
                xpassword = input()  # for login credentials

        elif short_code == 'cc':
            print("New user")
            print("-"*10)

            print("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()
            # create and save new user.
            save_users(create_user(f_name, l_name, p_number, e_address))
            print('\n')
            print(f"New user {f_name} {l_name} created")
            print('\n')

        elif short_code == 'dc':

            if display_users():
                print("Here is a list of all your users")
                print('\n')

                for user in display_users():
                    print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any users saved yet")
                print('\n')

        elif short_code == 'zc':

            if display_credentials():
                print(" list of all your login credentials you used before ")
                print('\n')

                for credentials in display_credentials():

                    print(f"{credentials.username} {credentials.pas} .....")

                    print('\n')

        elif short_code == 'ac':
                print("enter the name of credential you want to delete")
                search_application=input()
                if check_existing_credentials():
                    Credentials =find_credentials(search_application) 
                    del_credentials(Credentials)
                    print(f"{credentials.username} deleted")
                    print('\n')

                    print("credential and password deleted")
                else:
                    print("account name does not exist")  

        elif short_code == "ex":
            print("Thank You, See you Soon .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()


