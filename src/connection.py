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
    error.raise_connection_error(res);

    return res;
