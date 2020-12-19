import config
from controller import login
import os


def main(count):
    temp = count
    print(
        "|        welcome ro ATM app simulator      |"+"\n"
        "| please insert a card number and password |"+"\n"
    )


    n = input("card number => ").strip()
    p = input("card password => ").strip()

    login.login_check(n, p,temp)

