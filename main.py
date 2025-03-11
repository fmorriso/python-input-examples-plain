import sys
from input_utilities import InputUtils as IU

def get_python_version() -> str:
    """ the version of python running this program"""
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def ask_question_with_default_yes():
    """Ask yes/no question with Enter key meaning Yes"""
    yn = IU.get_yesno_response('Play again', enter = True)
    print(f'{yn=}')


def ask_question_with_default_no():
    """Ask yes/no question with Enter key meaning No"""
    yn = IU.get_yesno_response('Do you want to quit the program', enter = False)
    print(f'{yn=}')


def ask_question_with_no_default():
    """Ask yes/no question requiring explicit response"""
    yn = IU.get_yesno_response('Do you want ketchup')
    print(f'{yn=}')


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')

    ask_question_with_default_yes()
    ask_question_with_default_no()
    ask_question_with_no_default()
