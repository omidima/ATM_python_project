import config
import os
from core import func
from controller import c_t_c

def main():
    os.system("cls")
    print(
        "|                  cart to cart                   |"+"\n" +
        "|         please insert targer card numbe         |"+"\n" +
        "|-------------------------------------------------|"+"\n"
    )
    c2=input("target card number => ")
    money = input("cash to transfer ($) for cancell insert 0 => ")
    c_t_c.checker(c2, money)
    

