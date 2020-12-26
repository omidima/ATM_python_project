import config
import os
from controller import pc
from core import func


def main():
    print(
        "|               password change                |"+"\n" +
        "|          please insert new password          |"+"\n" +
        "|              inter 0 to exit app             |"+"\n" +
        "|----------------------------------------------|"+"\n" 
    )

    password = input("new Password => ")
    if password == "0":
        func.clossApp()
        return 0
    pc.changePass(password)
