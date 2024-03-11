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

ou informa atraves dp CLI argument '--lang'

ou o usuario tera que digitar
"""
__version__= "0.1.3"
__author__ = "Vanderson"
__license__ = "Unlicense"

#Este programa imprime Hello World
import os
import sys
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


arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use '=', you passed %s, try --key=value: %s",
            arg,
            str(e)
        )
        sys.exit(1)
        
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()
    arguments[key] = value
    
current_language = arguments["lang"]
if current_language is None:
    # TODO: usar repeticao
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language: ")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Ola, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language] * int(arguments["count"]))
