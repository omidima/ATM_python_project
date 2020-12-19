import config
import os
from view import home
from view import c_t_c



# card to card function
# read cash in 2 file and incress ,decreass
# @run: 1=> (money enough): success
# @run: 2=> (money not enough): unsuccess
# @run: 3=> (card invalid): error
# @load: view=>home
def c_t_c(num_1,num_2,count):
    try:
        f1 = open("data/"+num1+"/data.txt","r")
        f2 = open("data/"+num1+"/data.txt" ,"r")
        money_1 = f1.read().split(":")
        money_2 = f1.read().split(":")
        money_1 = money_1[1]-count
        if money_1>0:
            money_2 = money_2[1]+count
            f1 = open("data/"+num1+"/data.txt", "w")
            f2 = open("data/"+num1+"/data.txt", "w")
            f1.write("money:{}$".format(money_1))
            f2.write("money:{}$".format(money_2))
            os.system("cls")
            print("proccess successful")
            from view import home

        else:
            os.system("cls")
            print("you are not enough cash. please charge account")
            from view import home
    
    except :
        os.system("cls")
        print("incorrect card number please check again")
        from view import home



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
        
        
        
