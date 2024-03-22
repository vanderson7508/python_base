#!/usr/bin/env python3

"""
Faça um programa de terminal que exibe ao usuário uma listas dos quartos
disponiveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por virgulas.

`quartos.txt`
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

`reservas.txt`
# cliente, quarto, dias
Bruno,3,12

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
"""

import os
import sys

arguments = sys.argv[1:]

filename = arguments[0]
reservas_name = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
reservaspath = os.path.join(path, reservas_name)
codigos = []
while True:

    codigoo = []
    nomee = []
    precoo = []
    
    for line in open(filepath):
        if '#' not in line:
            codigo, nome, preco = line.split(",")
            print(f"Codigo {codigo}, nome: {nome}, preco: {preco}")

            codigoo.append(codigo)
            nomee.append(nome)
            precoo.append(preco)

    cod_esc = input("Qual o codigo do quarto que deseja alugar: ")
    if not cod_esc:
        break
        
    if int(cod_esc) not in codigos:
        codigos.append(int(cod_esc))
        qtd_dias = int(input("Qual a quantidade de dias: "))
        nome_cliente = input("Digite seu nome para reservar: ")
  

        valor_est = int(precoo[int(cod_esc) - 1]) * qtd_dias
        print()
        print(f"O valor total a pagar é {valor_est}")
        print(50 * '#')
        print()

        with open(reservaspath, "a") as file_:
                    file_.write(f"Cliente:{nome_cliente},\nQuarto:{nomee[int(cod_esc) - 1]},\nDias:{qtd_dias},\nValor total:{valor_est},\n\n ")
    else:
        print("Quarto ja foi reservado escolha outro!!!\n")           
            
