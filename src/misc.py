from src.error import ConnectionError, InputError;
from typing import *;
from random import randint;
import src.connection as connection;
import sys;

def get_user_choice() -> int:
    """Returns the choice of the user"""

    print ("What are you going to do?")
    print ("(1) Register        ");
    print ("(2) Login           ");
    print ("(3) Create Room     ");
    print ("(4) Get Room State  ");
    print ("(5) Send state event");
    print ("(6) Send a message  ");
    print ("(7) Send an invite  ");
    print ("(8) Sync data       ");
    print ("(9) Join a room     ");
    print ("(10) Get members    ");
    print ("(11) Get Messages   ");
    print ("(12) Print Messages");
    print ("(13) Logout         ");
    print ("(0) Quit            ");

    user_input = int(input("Your Choice: "));

    if (user_input > 13 or user_input < 0):
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
        (5) Send State Event
        (6) Send a message
        (7) Send an invite
        (8) Sync data
        (9) Join a room
        (10) Get members
        (11) Get messages
        (12) Print Messages
        (13) Logout
        (0) Exit
    """

    if (user_choice == 0):
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

        elif (user_choice == 6):
            room_id = input("Please enter room id: ");
            message = input("Please enter message: ");
            txn_id = str(randint(1, 1000000));
            res = connection.send_message (
                message,
                room_id,
                "m.room.message",
                txn_id,
                access_token
            );

        elif (user_choice == 7):
            room_id = input ("Please enter room id: ");
            user_id = input ("Please enter user id: ");
            res = connection.invite (
                room_id,
                user_id,
                access_token,
            );

        elif (user_choice == 8):
            res = connection.sync (access_token);

        elif (user_choice == 9):
            room_id = input ("Please enter room id: ");
            res = connection.join_room (room_id, access_token);

        elif (user_choice == 10):
            room_id = input ("Please enter room id: ");
            res = connection.get_members (room_id, access_token);

        elif (user_choice == 11 or user_choice == 12):
            room_id = input ("Please enter room id: ");
            res = connection.get_messages (room_id, access_token);
            if (user_choice == 12):
                messages = [(event["sender"], event["content"]["body"]) for event in res["chunk"] if "body" in event["content"]];
                messages.reverse();

                print ();
                print ("#" * 50);
                for sender, message in messages:
                    print (f"Sender: {sender}");
                    print (f"Message: {message}\n");
                print ("#" * 50);
                print ();

                res = {}

        elif (user_choice == 13):
            res = connection.logout_all (access_token);

    return res;
