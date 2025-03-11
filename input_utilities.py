import decimal
from decimal import Decimal


class InputUtils:

    @staticmethod
    def get_whole_number(prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except (TypeError, ValueError):
                print('Please enter a whole number')


    @staticmethod
    def get_whole_number_in_range(prompt: str, minimum: int = 0, maximum: int = 10) -> int:
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
        while True:
            try:
                return float(input(prompt))
            except (TypeError, ValueError):
                print('Please enter a number')


    @staticmethod
    def get_floating_point_number_in_range(prompt: str, minimum: int = 0, maximum: int = 10) -> float:
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
        while True:
            try:
                return Decimal(input(prompt))
            except (TypeError, ValueError):
                print('Please enter a decimal number')


    @staticmethod
    def get_decimal_number_in_range(prompt: str, minimum: int = 0, maximum: int = 10) -> decimal:
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
    def get_yesno_response(prompt: str, enter=None) -> bool:
        """get a yes/no (True/False) response to a question
        :param prompt: The yes/no question to ask the user
        :param enter: (optional) treat enter key as True or False.
        if True, hitting the Enter key is the same as Yes.
        if False, hitting the Enter key is the same as No.
        if not set, the user must explicitly enter yes/no/y/n
        """
        enter_key_meaning = ''
        if enter is None:
            enter_key_meaning = 'nothing'
        elif enter:
            enter_key_meaning = 'yes'
        elif not enter:
            enter_key_meaning = 'no'

        MSG: str = f'{prompt} (yes/y/no/n'#
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