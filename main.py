import src.connection as connection;
import src.misc as misc;
from pprint import pprint;
import sys;

def main():
    user_choice = misc.get_user_choice();
    res = misc.execute_user_choice (user_choice);
    pprint (res);

if __name__ == "__main__":
    main ();
