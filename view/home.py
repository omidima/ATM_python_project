import config
import os
from controller import home
from core import func

def main():

    print(
        "|                  home page                   |"+"\n" +
        "|           please select a function           |"+"\n" +
        "|----------------------------------------------|"+"\n" +
        "| 1 => cart to cart       2 => money left ouer |"+"\n" +
        "| 3 => change password    4 => recive money    |"+"\n" +
        "| 0 => close app                               |"+"\n"
    )


    s = input("select option => ")
    s = home.s_check(s)
    home.s_dir(s)



    
