import config
import os
from core import func
from view import home
from view import c_t_c
from view import mlo
from view import pc







def two(parameter_list):
    """
    docstring
    """
    pass


def there(parameter_list):
    """
    docstring
    """
    pass


def four(parameter_list):
    """
    docstring
    """
    pass


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
        home.main()
    else: 
        return select

# redirect to function view
# return: none
def s_dir(s):
    if s == "0":
        func.clossApp()
    elif s =="1":
        c_t_c.main()
    elif s == "2":
        mlo.main()
    elif s == "3":
        pc.main()
    
        
        
