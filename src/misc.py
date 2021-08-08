from typing import *

def get_user_choice() -> int:
    #################################################
    # Returns the choice of the user.               #
    #                                               #
    # user_input: int                               #
    #   The user's choice.                          #
    #                                               #
    #################################################

    print("What are you going to do?")
    print("(1) Register");
    print("(2) Login   ");
    print("(3) Quit    ");

    user_input = int(input("Your Choice: "));

    if (user_input > 3 or user_input < 1):
        raise Exception("Wrong Input");

    return user_input;

def get_user_pwd() -> Tuple[str, str]:
    #################################################
    # Prompts the user for the username and pwd.    #
    #                                               #
    # username: str                                 #
    #   The username                                #
    # pwd: str                                      #
    #   The password                                #
    #                                               #
    #################################################

    username = input("Enter username: ");
    pwd      = input("Enter password: ");

    return (username, pwd);
