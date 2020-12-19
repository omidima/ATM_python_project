import config
import os
from controller import home
from view import home
from core import func



def main():
    os.system("cls")
    print(
        "|                  cart to cart                   |"+"\n" +
        "|         please insert targer card numbe         |"+"\n" +
        "|-------------------------------------------------|"+"\n"
    )
    c2=input("target card number => ")
    money = input("cash to transfer ($)  => ")
    if c2 == "0":
        home.main()
    if func.number_check(c2) == True:
        c1 = func.getChash()
        home.c_t_c(c1, c2, money)
    else:
        print("card number incorrect please try again")
        os.system("cls")
        main()
    

