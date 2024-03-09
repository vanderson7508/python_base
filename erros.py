#!usr/bin/env python3

import sys
import os

# LBYL - Look Before you leap

if os.path.exists("names.txt"):
    print("O arquivo existe")
    input("...") # Race Condition
    names = open("names.txt").readlines()
else:
    print("[Error] File names.txt not found.")
    sys.exit(1)
    
if len(names) >= 5:
    print(names[5])
else:
    print("[Error]: Missing name in the list")
    sys.exit(1)
