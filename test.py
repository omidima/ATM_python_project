import config
from core import func

# open file and get data
# @return: array: [1]:special data [2]:special index [3]:all data
def getData():
    f = open("data/login.txt")
    a = f.readlines()
    temp = 0
    for i in range(len(a)):
        if "785786" in a[i]:
            temp = i
    return (a[temp].split(" ", 2),temp,a)


# change new password
# @input: data=>array newPass=>String
# @return: templeate String
def setPass(arr,newPass):
    t = []
    for i in arr:
        temp = i.split(":")
        if temp[0] == "password":
            temp[1] = newPass
        t.append(temp[1])
    return "number:{} password:{} name:{}".format(t[0], t[1], t[2])

# write data in login file
# @return: none
def setData(arr):
    f = open("data/login.txt", "w")
    for i in arr:
        # input(i)
        f.write(i)
        

def changePass(password):
    data = getData()
    temp_arr=data[2]
    temp_arr.pop(data[1])
    temp_arr.append(setPass(data[0], password))
    setData(temp_arr)





