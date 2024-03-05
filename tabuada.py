#!/usr/bin/env python
"""
Imprime a tabuada do 1 ao 10.

tabuada do 1-----
1 x 1 = 1
2 x 2 = 2
3 x 3 = 3

...
####################
tabuada do 2----
2 x 1 = 2
4 x 2 = 4
6 x 3 = 6
 
...
---------------------
"""
__version__ = "0.1.1"
__author__ = "Vanderson"


#base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros =list(range(1, 11))


# Iterable (percorriveis)

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 + n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
             
    print("#" * 18)
