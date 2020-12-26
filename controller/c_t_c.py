import config
import os
from core import func
from view import c_t_c
from view import home

# card to card function
# read cash in 2 file and incress ,decreass
# @run: 1=> (money enough): success
# @run: 2=> (money not enough): unsuccess
# @run: 3=> (card invalid): error
# @load: view=>home
def c(num_1, num_2, count):
    f1 = open("data/"+num_1+"/data.txt", "r")
    f2=None
    try:
        f2 = open("data/"+num_2+"/data.txt", "r")
    except:
        os.system("cls")
        print("card number incorrect please try again")
        return c_t_c.main()
    money_1 = f1.read().split(":")
    money_2 = f2.read().split(":")
    temp = money_change(money_1[1])
    if temp > int(count):
        os.system("cls")
        money_1 = money_change(money_1[1])-int(count)
        money_2 = money_change(money_2[1])+int(count)
        f_1 = open("data/"+num_1+"/data.txt", "w")
        f_2 = open("data/"+num_2+"/data.txt", "w")
        f_1.write("money:{}$".format(money_1))
        f_2.write("money:{}$".format(money_2))
        f_1.close()
        f_2.close()
        print("proccess successful")
        return home.main()
    else:
        os.system("cls")
        print("you are not enough cash. please charge account")
        return c_t_c.main()

def start(c2,money):
    if func.number_check(c2) == True:
        c1 = func.getChash()
        c(c1, c2, money)
    else:
        os.system("cls")
        print("card number incorrect please try again")
        return c_t_c.main()

# get param: string$
# @return: int
def money_change(num):
    temp=num.replace("$"," ")
    return int(temp)
