import os
from view import home

"""
# comment:
# login and signup function code
# this function for read a user information and return array

"""

# get account owner name
# @return: array
def getName():
    f = open("data/login.txt")
    arr_name = []
    name = f.readlines()
    for i in name:
        temp = i.split(" ", 2)
        for j in temp:
            t_2 = j.split(":")
            if t_2[0] == "name":
                arr_name.append(t_2[1])
    return arr_name

# get account owner password
# @return: array
def getPass():
    f = open("data/login.txt")
    arr_name = []
    name = f.readlines()
    for i in name:
        temp = i.split(" ", 2)
        for j in temp:
            t_2 = j.split(":")
            if t_2[0] == "password":
                arr_name.append(t_2[1])
    return arr_name

# get account owner card number
# @return: array
def getNumber():
    f = open("data/login.txt")
    arr_name = []
    name = f.readlines()
    for i in name:
        temp = i.split(" ", 2)
        for j in temp:
            t_2 = j.split(":")
            if t_2[0] == "number":
                arr_name.append(t_2[1])
    return arr_name


# create a directory and data.txt file for
# save user data
# @return: none
# @proccess: create dir=>number & file=>data.txt
def signup_data_create(number,D_money):
    path = "data/"+number
    try:
        f = open(path+"/data.txt", "r")
    except :
        os.mkdir(path)
        f = open(path+"/data.txt", "w")
        f.write("money:{}$".format(D_money))

# insert user login information
# @return: none
# @proccess: append (number,password,name) into file=>login.txt
def login_data_create(number,password,name):
    f = open("data/login.txt", "a")
    f.write("number:{} password:{} name:{} \n".format(number,password,name))

# card number check
# @return: boolean
def number_check(numebr):
    a = numebr
    if len(a.strip()) == 16:
        return True
    else:
        return False

# get card number in chash
# @return: string
def getChash():
    f=open("data/chash.txt","r")
    return f.read()

# set card number in chash
# @return: none
def setChash(n):
    f = open("data/chash.txt", "w")
    f.write(n)

# close app function
# @return:none
def clossApp():
    os.system("cls")
    print("Thansk for selection")

# cancell the proccess
# @return:none
def cancell():
    os.system("cls")
    return home.main()

# change money:@$ data to @
# @input: money data
# @return: string(int)
def cashChange(cash):
    money = cash.split(":")
    money = money[1].replace("$"," ")
    return money
    
