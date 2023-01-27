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
EXIT_COMMAND: List[str] = ['Quit', 'Q', 'Ex', 'Exit']
# Total purchase amount
PAYMENT: int = 0
# all goods
GOODS: List[str] = ['Apple', 'Cherry', 'Orange', 'Beef', 'Chicken', 'Lamb', 'Milk', 'Pasta', 'Rice']
# show items with numbers
NUMBERS_GOODS: Dict[str, int] = {'Apple': 100, 'Cherry': 100, 'Orange': 100, 'Beef': 100, 'Chicken': 100, 'Lamb': 100, 'Milk': 100, 'Pasta': 100, 'Rice': 100}  # noqaE E501
# show price of items
Price: Dict[str, int] = {'Apple': 25, 'Cherry': 50, 'Orange': 30, 'Beef': 200, 'Chicken': 100, 'Lamb': 300, 'Milk': 15, 'Pasta': 20, 'Rice': 120}               # noqaE E501


class Supermarket():

    def __str__(self):
        return self.username
    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.username}>'
    @staticmethod
    def help():
        with open('G:\django\class_project\helper\help.txt') as myfile:                                                                   # noqaE E501
            print(myfile.read())

    @staticmethod
    def category():
        with open('G:\django\class_project\helper\category.txt') as myfile:                                                           # noqaE E501
            print(myfile.read())

    @staticmethod
    def beautify_dict(shopping: Dict[str, int]) -> None:
        """
        Parameters
        ----------
        shopping: Dict[str : int] :
            Takes an entry in the form of a dictionary
        Returns
        -------
        the beautiful form for showing shopping list
        """
        for key, value in shopping.items():
            print(f'> {key} : {value}')

    @staticmethod
    def add_item(shopping: Dict[str, int], item: str, numbers: int) -> Dict[str, int]:                                              # noqaE E501
        """

        Parameters
        ----------
        shopping_dict : dict : Takes an entry in the form of a dictionary
            
        item : str : take the item that they want to add to shopping list
            
        numbers : int : take the number of the item that
            
        Returns
        -------
        return dict that its items are str, int
        """
        shopping[item] = numbers
        return shopping

    @staticmethod
    def remove_item(shopping: Dict[str, int], item: str) -> Dict[str, int]:
        """

        Parameters
        ----------
        shopping_dict : dict : Takes an entry in the form of a dictionary
            
        Returns
        -------
        return dict that its items are str, int
        """
        if item not in shopping:
            print('the item that you are trying remove is not in the list.')
        shopping.pop(item)
        return shopping

    @staticmethod
    def search_item(shopping: Dict[str, int], item: str) -> None:
        """

        Parameters
        ----------
        shopping_dict : list : Takes an entry in the form of a dictionary

        Returns
        -------
        None
        """
        if item in GOODS:
            if item in shopping:
                print(f'{item} is in your list')
            else:
                print('the item that you are trying to find is not in the list.')
        else:
            print('the item that you are trying to find is not in our stock.')

    @staticmethod
    def clear_screen():
        """clear the screen after any action"""
        return os.system('cls')

    @staticmethod
    def edit(shopping: Dict[str, int], previous_item: str, new_item: str, number_of_new_item: int) -> Dict[str, int]:                            # noqaE E501
        """

        Parameters
        ----------
        shopping_dict : Takes an entry in the form of a dictionary
            
        previous_item : take the  previous item that they want to delete it
            
        new_item : take the  new item that they want to replace it
            
        Returns
        -------
        return dict that its items are str, int
        """
        if previous_item not in shopping:
            print('the item that you are trying edit is not in the list.')
        shopping.pop(previous_item)
        shopping[new_item] = number_of_new_item
        return shopping

    @staticmethod
    def change_number(shopping: Dict[str, int], item: str, new_number: int) -> None:                                                                  # noqaE E501
        """

        Parameters
        ----------
        shopping_dict : Takes an entry in the form of a dictionary
            
        item : take the item that they want to change the number of it
            
        Returns
        -------
        None
        """
        shopping[item] = new_number

    @staticmethod
    def sort_order(shopping: Dict[str, int]) -> None:
        """

        Parameters
        ----------
        shopping: Dict[str : takes dict that its items are str, int
            
        Returns
        -------
        None
        """
        new_sort = sorted(shopping.items(), key=lambda x: x[1])
        for i in new_sort:
            print(i[0], i[1])

    @staticmethod
    def final(shopping: Dict[str, int]) -> None:
        """
        Parameters
        ----------
        shopping: Dict[str : int] : return dict that its items are str, int
            
        Returns
        -------
        None
        """
        print(shopping)

    def show_stock() -> None:
        """Shows the inventory to the user"""
        print(f'we have {NUMBERS_GOODS} now')


    def show_payment() -> None:
        """It shows the amount of payment required for the user at any moment"""
        print(f'you should pay {PAYMENT} until now')