class Error(Exception):
    """Base Class for exceptions"""
    pass

class ConnectionError(Error):
    """Raised when there is an Connection Error"""
    pass

class InputError(Error):
    """Raised when there is an Input Error"""
    pass

def raise_connection_error(result_dict: dict[str, str]) -> bool:
    """Raises a connection error

    Parameters
    ----------
    result_dict: dict[str, str]
        The result of the request
    """

    if ("errcode" in result_dict):
        raise ConnectionError (f"Error: {result_dict['errcode']}");

    return False;
