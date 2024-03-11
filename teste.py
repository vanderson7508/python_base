#!/usr/bin/env python3

"""
Programa para teste os recursos de leitura de arquivo
"""

import os
import sys

mensagem = input("Digite sua mensagem: ")

print(mensagem)

path = os.curdir
filepath = os.path.join(path, "mensagem.txt")

with open(filepath, "a") as arquivo:
    arquivo.write(f"{mensagem}\n")
