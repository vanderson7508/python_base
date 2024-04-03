#!usr/bin/env python3

import sys
import os
import logging
import time

log = logging.Logger("errors")


# LBYL - Look Before you leap
# EAFP - Easy to Ask Forgiveness than permission
# Race Condition
"""
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


def try_to_open_a_file(filepath, retry=1) -> list:
    #Tries to open a file, if error, retries n times
    for attempt in range(1, retry + 1):    
        try:
           return open(filepath).readlines() # FileNoFoundError
        except FileNotFoundError as e :
            log.error("ERRO: %s", e)
        else:
            print("Sucesso!!!")
        finally:
            print("Execute isso sempre")    
    return []

for line in try_to_open_a_file("names.txt"):
    print(line)    


def try_to_open_a_file(filepath, retry=1):
    for attempt in range(1, retry + 1):
        print(f"tentativa número {attempt}")
        try:
            return open(filepath).readline()
        except FileNotFoundError as e:
            log.error("ERRO %s", e)
            time.sleep(2)  
            # ^ isso aqui é só para fingir que estamos esperando um processo terminar
        else:
            print("Sucesso!!!")
        finally:
            print("Execute isso sempre!")
    return []


for line in try_to_open_a_file("names.txt", retry=5):
    print(line)

"""
def try_to_open_a_file(filepath, retry=1) -> list:
    """Tries to open a file, if error, retries n times."""
    if retry > 999:
        raise ValueError(
            "Retry cannot be above 999 because of Python recursion limit"
        )

    try:
        return open(filepath).readlines()  # FileNotFoundError
    except FileNotFoundError as e:
        log.error("ERRO: %s", e)
        time.sleep(2)
        if retry > 1:
            # recursão
            return try_to_open_a_file(filepath, retry=retry - 1)
    else:
        print("Sucesso!!!")
    finally:
        print("Execute isso sempre!")

    return []


for line in try_to_open_a_file("names.txt", retry=5):
    print(line)


