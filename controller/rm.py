import config
import os
from core import func
from view import rm
from view import home

def r_m(val):
    temp = input_check(val)
    c_num = func.getChash()
    f = open("data/"+c_num+"/data.txt", "r")
    money = func.cashChange(f.readline())
    f.close()
    money =int(money) - temp
    if money > 0:
        f = open("data/"+c_num+"/data.txt", "w")
        f.write("money:{}$".format(money))
        f.close()
        os.system("cls")
        print("procces ssuccessful \n")
        home.main()
    else:
        os.system("cls")
        print("you are not enough money \n")
        home.main()


def input_check(input):
    try:
        input = int(input)
        return input
    except:
        os.system("cls")
        print("value incorrect. please try again")
        rm.main()
