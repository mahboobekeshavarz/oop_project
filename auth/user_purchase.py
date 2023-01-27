from helper.exception import(
    WrongPasswordException,
    TypePasswordException,
    WrongUsernameException,
    TypeUsernameException,
    UsernameException
)

from typing import (List, Dict)
import os


# define the list
items: Dict = dict()


class Supermarket():
    """this class has some act for using in supermarket like adding product """
    # define the list
    items: Dict = dict()

    # exit command
    EXIT_COMMAND: List[str] = ['Quit', 'Q', 'Ex', 'Exit']

    # Total purchase amount
    PAYMENT: int = 0

    # all goods
    GOODS: List[str] = ['Apple', 'Cherry', 'Orange', 'Beef', 'Chicken', 'Lamb', 'Milk', 'Pasta', 'Rice']                                                             # noqaE E501

    # show items with numbers
    NUMBERS_GOODS: Dict[str, int] = {'Apple': 100, 'Cherry': 100, 'Orange': 100, 'Beef': 100, 'Chicken': 100, 'Lamb': 100, 'Milk': 100, 'Pasta': 100, 'Rice': 100}  # noqaE E501

    # show price of items
    Price: Dict[str, int] = {'Apple': 25, 'Cherry': 50, 'Orange': 30, 'Beef': 200, 'Chicken': 100, 'Lamb': 300, 'Milk': 15, 'Pasta': 20, 'Rice': 120}               # noqaE E501

    def __str__(self):
        return self.username

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.username}>'

    @staticmethod
    def help():
        """read file help that contains some sentences about helping costumer """                                               # noqaE E501
        with open('G:\django\class_project\helper\help.txt') as myfile:                                                                   # noqaE E501
            print(myfile.read())

    @staticmethod
    def category():
        """read file category that contains category of product in supermarket"""                                          # noqaE E501
        with open('G:\django\class_project\helper\category.txt') as myfile:                                                           # noqaE E501
            print(myfile.read())

    def beautify_dict(self, shopping: Dict[str, int]) -> None:
        """
        Parameters
        ----------
        shopping : Dict[str : int] : Takes an entry in the form of a dictionary
        Returns
        -------
        None
        """
        for key, value in shopping.items():
            print(f'> {key} : {value}')

    def add_item(self, shopping: Dict[str, int], item: str, numbers: int) -> Dict[str, int]:                                              # noqaE E501
        """
        Parameters
        ----------
        shopping_dict : dict : Takes an entry in the form of a dictionary
        item : str : take the item that they want to add to shopping list
        numbers: int : number of the items that costumer want to add to shopping list                                           # noqaE E501
        Returns
        -------
        DICT[str, int]
        """
        shopping[item] = numbers
        return shopping

    def remove_item(self, shopping: Dict[str, int], item: str) -> Dict[str, int]:                                                                      # noqaE E501
        """
        Parameters
        ----------
        shopping: Dict[str : int] : Takes an entry in the form of a dictionary
        item: str : a product that the user want to remove from shopping list
        Returns
        -------
        Dict[str, int]
        """
        if item not in shopping:
            print('the item that you are trying remove is not in the list.')
        shopping.pop(item)
        return shopping

    def search_item(self, shopping: Dict[str, int], item: str) -> None:
        """
        Parameters
        ----------
        shopping: Dict[str :int] : Takes an entry in the form of a dictionary
        item: str : the item that user want to search in shopping list
        Returns
        -------
        None
        """
        if item in User.GOODS:
            if item in shopping:
                print(f'{item} is in your list')
            else:
                print('the item that you are trying to find is not in the list.')                                             # noqaE E501
        else:
            print('the item that you are trying to find is not in our stock.')

    def clear_screen(self):
        """clear the screen after any action"""
        return os.system('cls')


    def edit(self, shopping: Dict[str, int], previous_item: str, new_item: str, number_of_new_item: int) -> Dict[str, int]:                            # noqaE E501
        """
        Parameters
        ----------
        shopping_dict : Takes an entry in the form of a dictionary
        previous_item : take the  previous item that they want to delete it
        number_of_new_item: int :
        Returns
        -------
        Dict[str, int]
        """
        if previous_item not in shopping:
            print('the item that you are trying edit is not in the list.')
        shopping.pop(previous_item)
        shopping[new_item] = number_of_new_item
        return shopping

    def change_number(self, shopping: Dict[str, int], item: str, new_number: int) -> None:                                                                  # noqaE E501
        """
        Parameters
        ----------
        shopping_dict : Takes an entry in the form of a dictionary
        Returns
        -------
        None
        """
        shopping[item] = new_number

    def sort_order(self, shopping: Dict[str, int]) -> None:
        """
        Parameters
        ----------
        shopping: Dict[str : int] : Takes an entry in the form of a dictionary
        Returns
        -------
        None
        """
        new_sort = sorted(shopping.items(), key=lambda x: x[1])
        for i in new_sort:
            print(i[0], i[1])

    def final(self, shopping: Dict[str, int]) -> None:
        """
        Parameters
        ----------
        shopping: Dict[str : int] : Takes an entry in the form of a dictionary
        Returns
        -------
        None
        """
        print(shopping)

    def show_stock(self) -> None:
        """Shows the inventory to the user"""
        print(f'we have {User.NUMBERS_GOODS} now')

    def show_payment(self) -> None:
        """It shows the amount of payment required for the user at any moment"""                                          # noqaE E501"""
        print(f'you should pay {User.PAYMENT} until now')


class User(Supermarket):
    """There are some actions that user can do in supermarket"""
    @property
    def username(self):
        """getter for username """
        return self.__username

    @username.setter
    def username(self, value):
        """
        Parameters
        ----------
        value : username
        Returns
        -------
        setter for username
        """
        if value == 'admin':
            raise UsernameException()
        if not isinstance(value, str):
            raise TypeUsernameException()
        if not value[0].isalpha():
            raise WrongUsernameException()
        self.__username = value

    @property
    def password(self):
        """get password """
        return self.__password

    @password.setter
    def password(self, value):
        """
        Parameters
        ----------
        value :
        password
        Returns
        -------
        setter for password
        """
        if not isinstance(value, int):
            raise TypePasswordException()
        if len(value) < 4:
            raise WrongPasswordException()
        self.__password = value

    def __str__(self):
        return self.username

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.username}>'

    def register(self, username, password):
        """
        Parameters
        ----------
        username : give username for register
        password : give password for register
        Returns
        -------
        """
        self.username = username
        self.password = password
        return self

    def check_details(self):
        """check details for logging user """
        username = input('USERNAME: ').casefold()
        password = input('PASSWORD: ')
        with open(r'G:\django\class_project\helper\user_data.txt') as myfile:
            info = myfile.read()
            info = info.split()
            if username in info:
                index = info.index(username) + 1
                usr_password = info[index]
                if usr_password == password:
                    print(f"Welcome Back,+ ' ' +{username}")
                    User.help()
                    budget = int(input('Enter your budget: '))
                    User.category()
                    while True:
                        item = input('enter the item to add to your list: ').title()                                                                     # noqaE E501
                        # clear the terminal screen
                        User.clear_screen(self)
                        # It checks item is in EXIT_COMMAND or not
                        if item in User.EXIT_COMMAND:
                            # after EXIT_COMMAND print the list
                            User.beautify_dict(self, items)
                            User.show_payment(self)
                            break
                        match item:
                            # see help command
                            case 'Help':
                                with open('G:\django\project_02\helper\help.txt') as myfile:                                             # noqaE E501
                                    print(myfile.read())
                            # show the items that are in the list
                            case 'Category':
                                with open('G:\django\project_02\helper\category.txt') as myfile:                                                             # noqaE E501
                                    print(myfile.read())
                            # show the price of goods
                            case 'Price':
                                with open('G:\django\project_02\helper\price.txt') as myfile:                                                          # noqaE E501
                                    print(myfile.read())
                            # show the stock
                            case 'Stock':
                                User.show_stock(self)
                            # show the total payment
                            case 'Payment':
                                User.show_payment(self)
                                # show items that you buy until now
                            case 'Show':
                                User.beautify_dict(self, items)
                            # sort items that you buy until now
                            case 'Sort':
                                User.sort_order(self, items)
                            # remove the item from the list
                            case 'Remove':
                                item_to_remove = input('enter the item to remove: ').title()                                                        # noqaE E501
                                # checks the input item for remove is in the shopping list                                                             # noqaE E501
                                if item_to_remove in items:
                                    # if the input item is in the shopping list, remove it                                                        # noqaE E501
                                    User.NUMBERS_GOODS[item_to_remove] += items[item_to_remove]                                                    # noqaE E501
                                    User.PAYMENT -= Price[item_to_remove] * items[item_to_remove]                                                         # noqaE E501
                                    User.remove_item(self, items, item_to_remove)                                                                 # noqaE E501
                                else:
                                    # check the input item is  in the shopping list                                                              # noqaE E501
                                    print(f'you dont have {item_to_remove} in your shopping list')                                               # noqaE E501
                            case 'Search':
                                # give the item for search
                                item_to_search = input('enter the item to search: ').title()                                                         # noqaE E501
                                # search for an item in the list
                                User.search_item(self, items, item_to_search)
                            case 'Edit':
                                # Takes the product, we want to change
                                previous_item = input('enter the item that you want to edit it: ').title()                                               # noqaE E501   
                                # It checks whether this amount is in the shopping list or not                                                  # noqaE E501
                                if previous_item in items:
                                    # He calculates the price of the product he wants to return                                                   # noqaE E501
                                    price_previous_item = items[previous_item] * User.Price[previous_item]                                                 # noqaE E501
                                    # Takes the value we want to replace
                                    new_item = input('enter the item that you want to replace: ').title()                                       # noqaE E501
                                    # Checks whether the new product is available in the store or not                                                 # noqaE E501
                                    if new_item in User.GOODS:
                                        # checks the new product is available in shopping list or not                                              # noqaE E501
                                        if new_item in items:
                                            # If the new product is in the shopping list, announce                                                  # noqaE E501
                                            print(f'{new_item} is already in your list!')                                                             # noqaE E501
                                        else:
                                            # it takes the desired number in the input                                                                    # noqaE E501
                                            number_new_item = \
                                            int(input(f'how many {new_item} do you want to add: '))                                                        # noqaE E501
                                            # calculate number of the new item in stock                                                                  # noqaE E501
                                            User.NUMBERS_GOODS[new_item] -= number_new_item                                                                 # noqaE E501
                                            # change the number of previous_item in stock                                                               # noqaE E501
                                            User.NUMBERS_GOODS[previous_item] += items[previous_item]                                            # noqaE E501
                                            # calculate the price of the new item                                                                   # noqaE E501
                                            price_new_item = number_new_item * User.Price[new_item]                                                        # noqaE E501
                                            # calculate the new budget
                                            User.PAYMENT = User.PAYMENT - price_previous_item + price_new_item                                                    # noqaE E501
                                            if User.PAYMENT > budget:
                                                # If the payment amount is more than the user's budget, it will announce the lack of budget                        # noqaE E501
                                                print(f'You have {User.PAYMENT - budget} less money')                                                            # noqaE E501
                                                # The user chooses to increase the budget or not                                                            # noqaE E501
                                                choice = input('if you want increase your budget, enter "YES" or otherwise enter "NO": ')                     # noqaE E501
                                                choice = choice.upper()
                                                if choice == 'YES':
                                                    # Enter the budget that she wants to increase                                                    # noqaE E501
                                                    more_budget = int(input('Enter your budget: '))                                                   # noqaE E501
                                                    budget = budget + more_budget                                                                     # noqaE E501
                                                    # The new product replaces the previous product                                                    # noqaE E501
                                                    User.edit(self, items, previous_item, new_item, number_new_item)                                               # noqaE E501
                                                else:
                                                    # they cannot change the product                                                                       # noqaE E501
                                                    print('you cant edit your product!')                                                                     # noqaE E501
                                                    User.PAYMENT = User.PAYMENT + price_previous_item - price_new_item                                      # noqaE E501
                                                    # change the number of new_item in stock                                                              # noqaE E501
                                                    User.NUMBERS_GOODS[new_item] += number_new_item                                                       # noqaE E501
                                                    # change the number of previous_item in stock                                                         # noqaE E501
                                                    User.NUMBERS_GOODS[previous_item] -= items[previous_item]                                             # noqaE E501
                                            # If the payment is enough, they can replace new product                                                          # noqaE E501
                                            else:
                                                User.edit(self, items, previous_item, new_item, number_new_item)                                                      # noqaE E501
                                    else:
                                        # the product that wants to replace is not in the store                                                             # noqaE E501
                                        print('we dont have that item you are trying to replace.')                                                             # noqaE E501
                                else:
                                    # if the previous product is not in the shopping list                                                                    # noqaE E501
                                    print(f'there is no {previous_item} in your list')                                                                       # noqaE E501
                            # change number of specific item
                            case 'Change_Number':
                                # Takes the name of the products that you want to change the number                                                         # noqaE E501
                                item_to_change = \
                                    input('enter the item that you want to chang its number: ').title()                                                      # noqaE E501
                                # takes the new number
                                number_to_change = \
                                    int(input(f'How many numbers of {item_to_change} do you want? '))                                                         # noqaE E501
                                # change the number of item in stock
                                User.NUMBERS_GOODS[item_to_change] = User.NUMBERS_GOODS[item_to_change] + items[item_to_change] - number_to_change                                                                         # noqaE E501
                                # chang the payment
                                User.PAYMENT = User.PAYMENT - items[item_to_change] * User.Price[item_to_change] + number_to_change * User.Price[item_to_change]                    # noqaE E501
                                # change number of item in shopping list
                                User.change_number(self, items, item_to_change, number_to_change)                                                             # noqaE E501
                            case 'Final':
                                # get fiNAL list
                                User.final(self, items)
                            case _:
                                # check if item exists in shopping list
                                if item in items:
                                    print('item is already in your list.')
                                # check if item exists in store
                                elif item not in User.GOODS:
                                    # if the product is not in the store, announce it                                                                             # noqaE E501
                                    print(f'we dont have {item}')
                                else:
                                    # if the product exits in the store, ask the number                                                                          # noqaE E501
                                    try:
                                        number = int(input('enter num: '))
                                        # Checks the desired quantity is available in store                                                                        # noqaE E501
                                        if number <= User.NUMBERS_GOODS[item]:
                                            # Calculates a payment
                                            User.PAYMENT += (number * User.Price[item])                                                                          # noqaE E501
                                            User.NUMBERS_GOODS[item] -= number
                                            # the payment is more than the budget or not                                                                         # noqaE E501
                                            if User.PAYMENT > budget:
                                                # it announce the lack of budget                                                                                  # noqaE E501
                                                print(f'You have {User.PAYMENT - budget} less money')                                                                  # noqaE E501
                                                # it asks if they wants to increase the budget or not                                                             # noqaE E501
                                                choice = input('if you want increase your budget, enter "YES" or if you want to continue enter "NO": ')            # noqaE E501
                                                choice = choice.upper()
                                                if choice == 'YES':
                                                    # Asks the amount of the budget increase                                                                      # noqaE E501
                                                    more_budget = int(input('Enter your budget: '))                                                                # noqaE E501
                                                    # calculate the new budget
                                                    budget = budget + more_budget                                                                                    # noqaE E501
                                                    # add the new item to the shopping list                                                                       # noqaE E501
                                                    User.add_item(self, items, item, number)                                                                                 # noqaE E501
                                                else:
                                                    # if user dont increase budget, calculate a payment                                                           # noqaE E501
                                                    User.PAYMENT -= (number * User.Price[item])                                                                   # noqaE E501
                                                    User.NUMBERS_GOODS[item] += number                                                                           # noqaE E501
                                                    print('you cant buy this product')                                                                           # noqaE E501
                                            else:
                                                # if the payment is enough, add it to shopping list                                                               # noqaE E501
                                                User.add_item(self, items, item, number)                                                                          # noqaE E501
                                                # It says the products that have been added to the list                                                           # noqaE E501
                                                print(f'{number} {item} add to your list')                                                                        # noqaE E501
                                                # It tells the number of products that have been purchased                                                        # noqaE E501
                                                print(f'there are {len(items)} type goods in your list')                                                          # noqaE E501
                                                # The number of products in stock is calculated                                                                   # noqaE E501
                                                User.show_payment(self)
                                                # It tells the amount paid by the user                                                                            # noqaE E501
                                                User.show_stock(self)
                                        # the requested product is more than the stock                                                                            # noqaE E501
                                        else:
                                            # announce number of items that user want in stock                                                                    # noqaE E501
                                            print(f'{number} of {item} is out of stock! enter stock.')                                                            # noqaE E501
                                    # show except if the user dont enter the number for product                                                                   # noqaE E501
                                    except ValueError:
                                        print('Oops! that was no valid number. Try again')                                                                       # noqaE E501
                else:
                    return "Password entered is wrong"
            else:
                return "Name not found. Please Sign Up."
