import requests
from typing import *

def login(username: str, password: str) -> dict[str, str]:
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
    res = requests.post(
            "http://localhost:8008/_matrix/client/api/v1/register",
            headers = {"ContentType": "application/json",
                        "charset": "utf-8"
            },
            json = {"user": username,
                    "password": password,
                    "type": "m.login.password"
            }
    );

    return res.json();

