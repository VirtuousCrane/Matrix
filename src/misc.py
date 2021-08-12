from typing import *

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
