#!usr/bin/env python3

import sys
import os

# LBYL - Look Before you leap
# EAFP - Easy to Ask Forgiveness than permission
# Race Condition

try:
    names = open("names.txt").readlines()
    # FileNoFoundError
except FileNoFoundError as e :
    print(f"{str(e)}.")
    sys.exit(1)
    #TODO: Usar retry
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre")    
try:
    print(names[4])
except:
    print("[Error]: Missing name in the list")
    sys.exit(1)
