import config
import os
from view import home
from view import c_t_c







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
    temp=1
    if len(select) < 0 or len(select) > 1:
        temp=0
    elif select != "1" or select != "2" or select != "3" or select != "4":
        temp=0
    if temp:
        os.system("cls")
        print("option invalid please try again")
        home.main()
    else: return select

# redirect to function view
# return: none
def s_dir(s):
    if s =="1":
        c_t_c.main()
        
        
        
