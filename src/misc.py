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
    print ("(4) Get Room State");
    print ("(5) Quit       ");

    user_input = int(input("Your Choice: "));

    if (user_input > 5 or user_input < 1):
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
        (4) Get Room State
        (5) Exit
    """

    if (user_choice == 5):
        sys.exit();

    username, pwd = get_user_pwd();

    if (user_choice == 1):
        res = connection.register (username, pwd);
    else:
        res = connection.login (username, pwd);
        if (user_choice == 3 or user_choice == 4):
            res = connection.create_room (res["access_token"]);
            if (user_choice == 4):
                res = connection.get_room_state(res["room_id"]);

    return res;
