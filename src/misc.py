from src.error import ConnectionError, InputError;
from typing import *;
import src.connection as connection;
import sys;

def get_user_choice() -> int:
    """Returns the choice of the user"""

    print ("What are you going to do?")
    print ("(1) Register   ");
    print ("(2) Login      ");
    print ("(3) Create Room");
    print ("(4) Quit       ");

    user_input = int(input("Your Choice: "));

    if (user_input > 4 or user_input < 1):
        raise InputError("Wrong Input");

    return user_input;

def get_user_pwd() -> Tuple[str, str]:
    """Gets the username and password of the user"""

    username = input ("Enter username: ").strip();
    pwd      = input ("Enter password: ").strip();

    return (username, pwd);

def execute_user_choice(user_choice: int) -> dict[str, str]:
    """Executes the choice of the user

    Parameters
    ----------
    user_choice: int
        The choice of the user
        (1) Register
        (2) Login
        (3) Create Room
        (4) Exit
    """

    if (user_choice == 4):
        sys.exit();

    username, pwd = get_user_pwd();

    if (user_choice == 1):
        res = connection.register (username, pwd);
    else:
        res = connection.login (username, pwd);
        if (user_choice == 3):
            res = connection.create_room (res["access_token"]);

    return res;
