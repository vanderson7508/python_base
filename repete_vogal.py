#!/usr/bin/env python3

"""
Repete vogal
"""
sair = True
palavras = []

while sair:
    palavra = input("Digite uma palavra: ").lower()
    if not palavra:
        break
        
    palavranova = ''
    for j in range(len(palavra)):
        if palavra[j] == 'a':
            palavranova += 'a' * 2
            
        elif palavra[j] == 'e':
            palavranova += 'e' * 2
            
        elif palavra[j] == 'i':
            palavranova += 'i' * 2

        elif palavra[j] == 'o':
            palavranova += 'o' * 2

        elif palavra[j] == 'u':
            palavranova += 'u' * 2
        else:
            palavranova += palavra[j]

    palavras.append(palavranova)
            

for i in palavras:
    print(i)
       
