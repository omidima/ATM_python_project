import config
import os
from core import func
from view import rm
from view import home
from view import c_t_c
from view import mlo
from view import pc




# select option checker
# @run: 1=> (1): try again
# @return: 2=> (0): selection
# @load: view=>home
def s_check(select):
    temp=0
    if "0"<=select<="5" :
        temp=1
    if temp == 0:
        os.system("cls")
        print("option invalid please try again")
        return home.main()
    else: 
        return select

# redirect to function view
# return: none
def s_dir(s):
    if s == "0":
        os.system("cls")
        return func.clossApp()
    elif s =="1":
        os.system("cls")
        return c_t_c.main()
    elif s == "2":
        os.system("cls")
        return mlo.main()
    elif s == "3":
        os.system("cls")
        return pc.main()
    elif s == "4":
        os.system("cls")
        return rm.main()
