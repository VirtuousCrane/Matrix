import requests
from typing import *

def login(username: str, password: str) -> dict[str, str]:
    """This function attempts to connect to the server and login

    Parameters
    ----------
    username : str
        The username of the user
    password : str
        The password of the user
    """

    res = requests.post(
            "http://localhost:8008/_matrix/client/api/v1/login",
            headers = {"ContentType": "application/json",
                        "charset": "utf-8"
            },
            json = {"user": username,
                    "password": password,
                    "type": "m.login.password"
            }
    );

    return res.json();

def register(username: str, password: str) -> dict[str, str]:
    """This function attempts to connect to the server and login

    Parameters
    ----------
    username : str
        The username of the user
    password : str
        The password of the user
    """

    res = requests.post(
            "http://localhost:8008/_matrix/client/r0/register",
            headers = {"ContentType": "application/json",
                        "charset": "utf-8"
            },
            json = {"username": username,
                    "password": password,
                    "type": "m.login.password"
            }
    );

    res = res.json();

    return res.json();

