#!/usr/bin/env python3

__version__= "0.1.0"
__author__ = "Vanderson"
__license__ = "Unlicense"
"""
MINHA SOLUCAO

import os
import sys


arguments = {"operacao": None, "n1": None, "n2": None}

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()
    arguments[key] = value

operacao = arguments["operacao"]

while operacao != 'sum' and operacao != 'sub' and operacao != 'mul' and operacao != 'div':
    operacao = input("Digite a operacao: ")

if operacao == 'sum':
    soma = float(arguments["n1"]) + float(arguments["n2"])
    print(soma)
    
elif operacao == 'sub':
    subt = float(arguments["n1"]) - float(arguments["n2"])
    print(subt)
    
elif operacao == 'mul':
    mult = float(arguments["n1"]) * float(arguments["n2"])
    print(mult)

elif operacao == 'div':
    divi = float(arguments["n1"]) / float(arguments["n2"])
    print(divi)
"""
"""
Os resultados serao salvos em 'prefixcalc.log'
"""

import sys
import os
from datetime import datetime
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("vanderson", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'  
)
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = sys.argv[1:]

valid_operations = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}

path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

while True:

    if not arguments:
        operation = input("operacao: ")
        n1 = input("n1: ")
        n2 = input("n2: ")
        arguments = [operation, n1, n2]
        
    elif len(arguments) != 3:
        print("Numero de argumentos invalidos")
        print("ex: 'sum 5 5'")
        sys.exit(1)

    operation, *nums = arguments

    if operation not in valid_operations:
        print("Operacao invalida")
        print(valid_operations)
        sys.exit(1)

    validated_nums = []
    for num in nums:
        if not num.replace(".","").isdigit():
            print(f"Numero invalido {num}")
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num)
    try:
        n1, n2 = validated_nums
    except ValueError as e:
        print(str(e))
        sys.exit(1)
   
    result = valid_operations[operation](n1, n2)
    print(f"O resultado é {result}")

    try:
        with open(filepath, "a") as file_:
            file_.write(f"{timestamp} - {user} -  {operation}, {n1}, {n2} = {result}\n")
    except PermissionError as e:
        log.error(
            "voce nao tem acesso para ler o arquivo %s",
            str(e)
        )
        sys.exit(1)

    if  input("Pressione enter para continuar ou qualquuer tecla para sair  "):
        break

