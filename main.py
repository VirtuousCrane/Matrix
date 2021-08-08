import src.connection as connection
import src.misc as misc
import sys

def main():
    user_choice = misc.get_user_choice();

    if (user_choice == 3):
        sys.exit();

    username, pwd = misc.get_user_pwd();

    if (user_choice == 2):
        res = connection.login(username, pwd);
    elif (user_choice == 1):
        res = connection.register(username, pwd);
    print(res);

if __name__ == "__main__":
    main();
