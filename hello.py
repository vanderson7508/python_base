#!/usr/bin/env python3
"""
Hello World Multi Linguas.

Dependendo da LINGUA CONFIGURADA no ambiente o programa exibe a mensagem
correspondente.

Como usar:

tenha a variaVEL LANG devidamente configurada ex:

    export LANG=pt_BR

Execucao:

    python3 hello.py
    ou
    ./hello.py

if __name__ == "__main__":
"""
__version__= "0.0.1"
__author__ = "Vanderson"
__license__ = "Unlicense"

#Este programa imprime Hello World
import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"


print(msg)
