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


def c_t_c(num_1, num_2, count):
    try:
        f1 = open("data/"+num_1+"/data.txt", "r")
        f2 = open("data/"+num_2+"/data.txt", "r")
        money_1 = f1.read().split(":")
        money_2 = f2.read().split(":")
        f1.close()
        f2.close()
        temp = money_change(money_1[1])
        if temp > int(count):
            os.system("cls")
            money_1 = money_change(money_1[1])-int(count)
            money_2 = money_change(money_2[1])+int(count)
            f1 = open("data/"+num_1+"/data.txt", "w")
            f2 = open("data/"+num_2+"/data.txt", "w")
            f1.write("money:{}$".format(money_1))
            f2.write("money:{}$".format(money_2))
            
            print("proccess successful")
            home.main()
        else:
            os.system("cls")
            print("you are not enough cash. please charge account")
            home.main()

    except:
        os.system("cls")
        print("incorrect card number please check again")
        home.main()

def checker(c2,money):
    if c2 == "0":
        home.main()
    if func.number_check(c2) == True:
        c1 = func.getChash()
        c_t_c(c1, c2, money)
    else:
        print("card number incorrect please try again")
        os.system("cls")
        home.main()

def money_change(num):
    temp=num.replace("$"," ")
    return int(temp)


c_t_c("6037998143622743","6037997468139911",5)
