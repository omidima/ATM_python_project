import config
import os
from controller import pc


def main():
    print(
        "|               password change                |"+"\n" +
        "|          please insert new password          |"+"\n" +
        "|----------------------------------------------|"+"\n" 
    )

    password = input("new Password => ")
    pc.changePass(password)
