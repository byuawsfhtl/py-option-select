"""
File: menu.py
Author: Kevin Richins
Date: 3/11/2024
Description: This file contain the menu class that outputs options and ensures correct user input.
"""
from collections import namedtuple
from typing import NamedTuple
class Menu:
    """Class for interacting with the user. Prints menus and ensures correct input.

    Attributes:
    """
    def __init__(self) -> None:
        """Initializes menu class.
        """

    def interactWithMenu(self, connected: bool, action: str, output: list, option: str, notConnectedErrorMessage: str='Condition not passed') -> NamedTuple:
        """Prints a given menu and ensures correct user input.

        Args:
            connected (bool): whether or not a file is loaded into csvScraper
            action (str): description of what to ask the user to do
            output (list): a list of tuples with four items in each tuple;this is the actual body of the menu
            option (str): what the user can type in to return to exit the current function

        Returns:
            NamedTuple: values(returnVal, args, optionSelected)

        Notes:
            The output list of tuples is in this format: string to print, value to get if this option is selected, boolean of whether a file is needed for the current function, and arguments in a list for the second value if needed.
        """
        menuTup = namedtuple('mt', ['returnVal', 'args', 'optionSelected'])
        while True:
            #print the action output and option
            print(f'\n{action}')
            for index, item in enumerate(output):
                print(f'{index+1}: {item[0]}')
            #get the user input
            choice = input(f'Enter number 1-{len(output)} or {option}: ')

            #subtract 1 if user gave us a number
            if choice.isnumeric():
                choice = int(choice)
                choice -= 1
            #if user chose the option return with optionSelected = True
            elif choice == option:
                return menuTup(option, [], True)
            else:
                print('\nERROR: Please enter a number!')
                continue
            
            #check to see if the user gave us a number that is too big or small
            if choice < 0 or choice + 1 > len(output):
                print('ERROR: Please enter a valid number!')
                continue

            #check to see if the requested action needs a file loaded to work
            if output[choice][2] == True:
                if connected == False:
                    print('\nERROR: ' + notConnectedErrorMessage)
                    continue

            return menuTup(output[choice][1], output[choice][3], False)