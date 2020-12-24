import config
import os
from core import func
from controller import signup

def main():

    print(
        "|        welcome to ATM app simulator      |"+"\n"
        "|  before signup in app input custom card  |"+"\n"
        "|  number by 16 lengh and insert password  |"+"\n"
        "|------------------------------------------|"+"\n"
    )

    number = input("input card number len(16) => ")
    password = input("insert a password => ")
    money = input("insert a first defult money ($) => ")
    name = input("insert your name => ")
    val = {"number":number,"password":password,"money":money,"name":name}
    signup.n_c(val)


