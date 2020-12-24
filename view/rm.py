import config
import os
from controller import rm
from core import func


def main():

    print(
        "|                 recive money                 |"+"\n" +
        "|           please inter count money           |"+"\n" +
        "|----------------------------------------------|"+"\n" 
    )

    val = input("inter count ($) only integer => ")
    rm.r_m(val)
    