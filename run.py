from auth import User
from helper.exception import(
    WrongPasswordException,
    TypePasswordException,
    WrongUsernameException,
    TypeUsernameException,
    UsernameException
)

user1 = User()


def choices():
    """there are some choices for user. when this action run, user choose 1 or 2 for sign up or sign in """                                  # noqaE E501
    print("Please choose what would you like to do?")
    choice = int(input("For Signing Up Type 1 and For Signing in Type 2: "))
    if choice == 1:
        return get_details()
    elif choice == 2:
        return User.check_details(user1)
    else:
        raise TypeError('you should choose 1 or 2.')


def get_details():
    """ in this part user enter its username and password for signing up"""
    try:
        username = input('USERNAME: ').casefold()
        password = input('PASSWORD: ')
        with open(r'G:\django\class_project\helper\user_data.txt') as myfile:
            info = myfile.read()
            if username in info:
                print("Name Unavailable. Please Try Again")
            else:
                user1.register(username, password)
                with open(r'G:\django\class_project\helper\user_data.txt', 'a') as myfile:                                                # noqaE E501
                    new_info = " " + username + " " + password
                    myfile.write(new_info)
                print('you are registered successfully')

    except WrongPasswordException as e:
        print(e)
    except TypePasswordException as e:
        print(e)
    except WrongUsernameException as e:
        print(e)
    except TypeUsernameException as e:
        print(e)
    except UsernameException as e:
        print(e)


print(choices())
