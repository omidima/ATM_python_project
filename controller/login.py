import config
import os
from core import func
from view import home
from view import login

def login_check(username,password,temp):
    n = func.getNumber()
    p = func.getPass()
    na = func.getName()
    check=None
    for i in range(len(n)):
        if n[i] == username and p[i] == password:
            check = username
    if check != None:
        func.setChash(check)
        home.main()
    else:
        os.system("cls")
        print("information incorrect please try again \n")
        temp-=1
        if temp > 0:
            login.main(temp)
        else:
            os.system("cls")
            print("you cant login to app")
        

def load_start():
    os.system("cls")
    login.main(3)


