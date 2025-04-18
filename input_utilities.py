import decimal
from decimal import Decimal
from typing import Union


class InputUtils:

    @staticmethod
    def get_whole_number(prompt: str) -> int:
        """
        Get a whole number (unrestricted range).
        :param prompt:  A string containing the prompt text to show the user.
        :return: a whole value
        """
        while True:
            try:
                return int(input(prompt))
            except (TypeError, ValueError):
                print('Please enter a whole number')


    @staticmethod
    def get_whole_number_in_range(prompt: str, minimum: int = 0, maximum: int = 10) -> int:
        """
        Get a whole number with a restricted range of values.
        :param prompt:  A string containing the prompt text to show the user.
        :param minimum: The minimum value that can be entered.
        :param maximum: The maximum value that can be entered.
        :return: a whole value
        """
        MSG: str = f'{prompt} (between {minimum} and {maximum}) '
        while True:
            try:
                n = int(input(MSG))
                if minimum <= n <= maximum:
                    return n
                print(f'Please enter a number between {minimum} and {maximum}')
            except (TypeError, ValueError):
                print('Please enter a whole number')


    @staticmethod
    def get_floating_point_number(prompt: str) -> float:
        """
        Get a floating point number (unrestricted range).
        :param prompt:  A string containing the prompt text to show the user.
        :return: a floating point value
        """
        while True:
            try:
                return float(input(prompt))
            except (TypeError, ValueError):
                print('Please enter a number')


    @staticmethod
    def get_floating_point_number_in_range(prompt: str, minimum: float = 0, maximum: float = 10) -> float:
        """
        Get a floating point number with a restricted range of values.
        :param prompt:  A string containing the prompt text to show the user.
        :param minimum: The minimum value that can be entered.
        :param maximum: The maximum value that can be entered.
        :return: a floating point value
        """
        MSG: str = f'{prompt} (between {minimum} and {maximum}) '
        while True:
            try:
                n = float(input(MSG))
                if minimum <= n <= maximum:
                    return n
                print(f'Please enter a number between {minimum} and {maximum}')
            except (TypeError, ValueError):
                print('Please enter a number')


    @staticmethod
    def get_decimal_number(prompt: str) -> decimal:
        """
        Get a decimal number (unrestricted range).
        :param prompt:  A string containing the prompt text to show the user.
        :return: a decimal value
        """
        while True:
            try:
                return Decimal(input(prompt))
            except (TypeError, ValueError):
                print('Please enter a decimal number')


    Number_with_decimal_point = Union[float, Decimal]  # input parameter type with some flexibility


    @staticmethod
    def get_decimal_number_in_range(prompt: str, minimum: Number_with_decimal_point = 0,
                                    maximum: Number_with_decimal_point = 10) -> decimal:
        """
        Get a decimal number with a restricted range of values.
        :param prompt:  A string containing the prompt text to show the user.
        :param minimum: The minimum value that can be entered.
        :param maximum: The maximum value that can be entered.
        :return: a decimal value
        """
        MSG: str = f'{prompt} (between {minimum} and {maximum})'
        while True:
            try:
                n = Decimal(input(MSG))
                if minimum <= n <= maximum:
                    return n
                print(f'Please enter a number between {minimum} and {maximum}')
            except (TypeError, ValueError):
                print('Please enter a decimal number')


    @staticmethod
    def get_yesno_response(prompt: str, enter = None) -> bool:
        """get a yes/no (True/False) response to a question
        :param prompt: The yes/no question to ask the user
        :param enter: (optional) treat enter key as True or False.
        if True, hitting the Enter key is the same as Yes.
        if False, hitting the Enter key is the same as No.
        if not set, the user must explicitly enter yes/no/y/n

        Example usage:
            ``from input_utilities import InputUtils as IU``
            ``yn = IU.get_yesno_response('Do you want ketchup')``
            ``yn = IU.get_yesno_response('Play again', enter = True)``
            ``yn = IU.get_yesno_response('Do you want to quit the program', enter = False)``
        """
        enter_key_meaning = ''
        if enter is None:
            enter_key_meaning = 'nothing'
        elif enter:
            enter_key_meaning = 'yes'
        elif not enter:
            enter_key_meaning = 'no'

        MSG: str = f'{prompt.replace('?', '', 1)} (yes/y/no/n'  #
        if enter_key_meaning == 'nothing':
            MSG += ') ?'
        elif enter_key_meaning == 'yes':
            MSG += ', Enter key means Yes) ?'
        elif enter_key_meaning == 'no':
            MSG += ', Enter key means No) ?'

        while True:
            try:
                response = input(MSG)
                if len(response) == 0:
                    if enter_key_meaning == 'yes':
                        return True
                    if enter_key_meaning == 'no':
                        return False
                    print('You must enter something. Try again')
                elif response.lower() in ('y', 'yes'):
                    return True
                elif response.lower() in ('n', 'no'):
                    return False
                else:
                    print('Invalid response. Try again')
            except Exception:
                print('Please enter a valid response')
