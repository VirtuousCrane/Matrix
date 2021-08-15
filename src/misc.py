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
    print ("(5) Send state event");
    print ("(6) Quit       ");

    user_input = int(input("Your Choice: "));

    if (user_input > 6 or user_input < 1):
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

    if (user_choice == 6):
        sys.exit();

    username, pwd = get_user_pwd();

    if (user_choice == 1):
        res = connection.register (username, pwd);
    else:
        res = connection.login (username, pwd);
        access_token = res["access_token"];

        if (user_choice == 3):
            res = connection.create_room (access_token);

        elif (user_choice == 4):
            room_id = input ("Please enter room id: ");
            res = connection.get_room_state (room_id, access_token);

        elif (user_choice == 5):
            room_id = input ("Please enter room id: ");
            event_type = input ("Please enter event type: ");
            state_key = input ("Please enter state key: ");
            res = connection.send_room_event (
                room_id,
                event_type,
                state_key,
                access_token
            );

    return res;
