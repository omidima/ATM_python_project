import config
import os
from controller import rm
from core import func


def main():

    print(
        "|                 recive money                 |"+"\n" +
        "|           please inter count money           |"+"\n" +
        "|          inter 0 to cancell proccess         |"+"\n" +
        "|----------------------------------------------|"+"\n" 
    )

    val = input("inter count ($) only integer => ")
    if val == "0":
        func.cancell()
        return 0
    rm.r_m(val)
    
