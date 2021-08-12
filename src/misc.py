from typing import *

class Error(Exception):
    """Base Class for exceptions"""
    pass

class ConnectionError(Error):
    """Raised when there is a Connection Error"""
    pass

def get_user_choice() -> int:
    """Returns the choice of the user"""

    print("What are you going to do?")
    print("(1) Register");
    print("(2) Login   ");
    print("(3) Quit    ");

    user_input = int(input("Your Choice: "));

    if (user_input > 3 or user_input < 1):
        raise Exception("Wrong Input");

    return user_input;

def get_user_pwd() -> Tuple[str, str]:
    """Gets the username and password of the user"""

    username = input("Enter username: ").strip();
    pwd      = input("Enter password: ").strip();

    return (username, pwd);

def raise_matrix_error(result_dict: dict[str, str]):
    """Raises an error if there is one

    Parameters
    ----------
    result_dict: dict[str, str]
        The dictionary that comes from making a request
    """

    if ("errcode" in result_dict):
        raise ConnectionError(f"Error: {result_dict['errcode']}");
