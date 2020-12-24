import config
from controller import login
import os



def main(count):
    temp = count
    print(
        "|        welcome ro ATM app simulator      |"+"\n"
        "| please insert a card number and password |"+"\n"
        "| and if you want signp to app click on 0  |"+"\n"+
        "|------------------------------------------|"+"\n"
    )


    n = input("card number => ").strip()
    if n == "0":
        login.load_signup()
    else:
        p = input("card password => ").strip()
        login.login_check(n, p,temp)

