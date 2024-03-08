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
__version__= "0.1.2"
__author__ = "Vanderson"
__license__ = "Unlicense"

#Este programa imprime Hello World
import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Ola, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language])
