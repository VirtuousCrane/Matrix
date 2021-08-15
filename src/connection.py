import requests;
import src.misc as misc;
import src.error as error;
from typing import *;

def login(username: str, password: str) -> dict[str, str]:
    """This function attempts to connect to the server and login

    Parameters
    ----------
    username : str
        The username of the user
    password : str
        The password of the user
    """

    res = requests.post (
        "http://localhost:8008/_matrix/client/r0/login",
        json = {
            "type": "m.login.password",
            "user": username,
            "password": password
        }
    );

    res = res.json();
    error.raise_connection_error(res);

    return res;

def register_auth(username: str, password: str, session: str) -> dict[str, str]:
    """Authenticates the registration against the server

    Parameters
    ----------
    username : str
        The username of the user
    password : str
        The password of the user
    session : str
        The session authentication code
    """

    res = requests.post (
        "http://localhost:8008/_matrix/client/r0/register",
        json = {
            "auth": {
                "type": "m.login.dummy",
                "session": session,
            },
            "username": username,
            "password": password,
        }
    );

    res = res.json();
    error.raise_connection_error(res);

    return res;

def register(username: str, password: str) -> dict[str, str]:
    """This function attempts to connect to the server and register a user

    Parameters
    ----------
    username : str
        The username of the user
    password : str
        The password of the user
    """

    res = requests.post (
        "http://localhost:8008/_matrix/client/r0/register",
        json = {"username": username,
                "password": password,
        }
    );

    res = res.json();
    error.raise_connection_error(res);
    res = register_auth (username, password, res["session"]);

    return res;

def create_room(access_token: str) -> dict[str, str]:
    """Creates a new Matrix room

    Parameters
    ----------
    access_token: str
        The access token of the user
    """

    res = requests.post (
        "http://localhost:8008/_matrix/client/r0/createRoom" +
        "?access_token=" +
        access_token,
        json = {
        },
    );

    res = res.json();
    error.raise_connection_error (res);

    return res;

def get_room_state(room_id: str, access_token: str) -> dict[str, str]:
    """Gets the room state

    Parameters
    ----------
    room_id: str
        The room's id
    access_token: str
        The access token we have previously acquired from logging in
    """

    url = f"http://localhost:8008/_matrix/client/r0/rooms/{room_id}/state?access_token={access_token}";
    res = requests.get (url);
    res = res.json();
    error.raise_connection_error (res);

    return res;

def send_room_event(
        room_id: str,
        event_type: str,
        state_key: str,
        access_token: str
    ) -> dict[str, str]:
    """Sends a state event into the room

    Parameters
    ----------
    room_id: str
        The room's id
    event_type: str
        The type of event we want to fire into the room
    state_key: str
        The state key
    access_token: str
        The access token we have previously acquired from logging in
    """

    url = f"http://localhost:8008/_matrix/client/r0/rooms/{room_id}/state/{event_type}/{state_key}?access_token={access_token}";
    res = requests.put (url, json = { "baz": "qux" });
    res = res.json();
    error.raise_connection_error (res);

    return res;

def send_message(
    message: str,
    room_id: str,
    event_type: str,
    txn_id: str,
    access_token: str
) -> dict[str, str]:
    """Sends a message

    Parameters
    ----------
    message: str
        The message we want to send
    room_id: str
        The room's id
    event_type: str
        The type of the event
    txn_id: str
        The transaction id
    access_token: str
        The access token we have previously acquired from logging in
    """

    url = f"http://localhost:8008/_matrix/client/r0/rooms/{room_id}/send/{event_type}/{txn_id}?access_token={access_token}";
    res = requests.put (
        url,
        json = {
            "msgtype": "m.text",
            "body": message,
        }
    );
    res = res.json();
    error.raise_connection_error (res);

    return res;

def invite(
    room_id: str,
    user_id: str,
    access_token: str
) -> dict[str, str]:
    """Invites someone into a room

    Parameters
    ----------
    room_id: str
        The room's id
    user_id: str
        The id of the user we want to invite
    access_token: str
        The access token we have previously acquired from logging in
    """

    url = f"http://localhost:8008/_matrix/client/r0/rooms/{room_id}/invite?access_token={access_token}";
    res = requests.post (
        url,
        json = {
            "user_id": user_id
        }
    );
    res = res.json();
    error.raise_connection_error (res);

    return res;

def sync(access_token: str) -> dict[str, str]:
    """Syncs a user's data

    Parameters
    ----------
    access_token: str
        The access token we have previously acquired from logging in
    """

    url = f"http://localhost:8008/_matrix/client/r0/sync?access_token={access_token}";
    res = requests.get (url);
    res = res.json();
    error.raise_connection_error (res);

    return res;

def join_room(room_id: str, access_token: str) -> dict[str, str]:
    """Joins a room

    Parameters
    ----------
    room_id: str
        The id of the room that we are going to join
    access_token: str
        The access token we have previously acquired from logging in
    """

    url = f"http://localhost:8008/_matrix/client/r0/rooms/{room_id}/join?access_token={access_token}";
    res = requests.post (url);
    res = res.json();
    error.raise_connection_error (res);

    return res;
