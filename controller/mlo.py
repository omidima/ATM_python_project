import config
import os
from view import home

def getCashInfo():
    f = open("data/chash.txt","r")
    c_num = f.readline()

    f = open("data/"+c_num+"/data.txt", "r")
    money = f.readline()
    os.system("cls")
    print("left over your account = ",getCash(money),end="\n")
    home.main()


def getCash(c):
    money = c.split(":")
    return money[1]

