import sys
from input_utilities import InputUtils as IU

def get_python_version() -> str:
    """ the version of python running this program"""
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def ask_question_with_default_yes():
    """Ask yes/no question with Enter key meaning Yes"""
    yn = IU.get_yesno_response('Play again?', enter = True)
    print(f'{yn=}')


def ask_question_with_default_no():
    """Ask yes/no question with Enter key meaning No"""
    yn = IU.get_yesno_response('Do you want to quit the program?', enter = False)
    print(f'{yn=}')


def ask_question_with_no_default():
    """Ask yes/no question requiring explicit response"""
    yn = IU.get_yesno_response('Do you want ketchup?')
    print(f'{yn=}')


def ask_for_whole_number():
    """Ask for a whole number with no restrictions"""
    n = IU.get_whole_number('How many people are in your party? ')
    print(f'{n=}')


def ask_for_whole_number_in_range():
    """Ask for a whole number with a range restriction"""
    n = IU.get_whole_number_in_range('How many people are in your party? ', 1, 7)
    print(f'{n=}')


def ask_for_floating_point_number():
    """Ask for a floating point number with no restrictions"""
    x = IU.get_floating_point_number('What was the weight in pounds? ')
    print(f'{x=}')

def ask_for_floating_point_number_in_range():
    """Ask for a floating point number with a range restriction"""
    x = IU.get_floating_point_number_in_range('How many gallons do you wish to purchase? ', 0.5, 22.5)
    print(f'{x=}')


def ask_for_decimal_number():
    """Ask for a decimal number with no restrictions"""
    d = IU.get_decimal_number('How much money do you wish to withdraw? ')
    print(f'{d=:,.2f}')


def ask_for_decimal_number_in_range():
    """Ask for a decimal number with a range restriction"""
    d = IU.get_decimal_number_in_range('How much money do you wish to withdraw? ', 5, 600)
    print(f'{d=:,.2f}')

if __name__ == '__main__':
    print(f'Python version {get_python_version()}')

    # ask_question_with_default_yes()
    ask_question_with_default_no()
    ask_question_with_no_default()

    ask_for_whole_number()
    ask_for_whole_number_in_range()

    ask_for_floating_point_number()
    ask_for_floating_point_number_in_range()

    ask_for_decimal_number()
    ask_for_decimal_number_in_range()