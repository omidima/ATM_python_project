import config
import os
from core import func
from view import signup
from view import login


# input a dictionary of data
# data: number=> card number, password => card password, money=> defult money, name=> user name
def n_c(dictionary):
    func.number_check(dictionary["number"])
    val = m_value_chack(dictionary["money"])
    func.signup_data_create(dictionary["number"],val)
    func.login_data_create(
        dictionary["number"], dictionary["password"], dictionary["name"])
    os.system("cls")
    print("proccess successful \n")
    return login.main(3)

    


def m_value_chack(n):
    try:
        temp = int(n)
        return n
    except:
        os.system("cls")
        print("money incorrecty value. please try again")
        signup.main()



