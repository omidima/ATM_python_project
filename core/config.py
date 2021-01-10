"""
# comment:
# config to file control path
# get directory path and append address to system path

"""
try:
    import os
    import sys
    p = os.getcwd()
    sys.path.append(p)
except:
    print("module import not success please check config file")