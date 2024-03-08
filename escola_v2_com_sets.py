#!/usr/bin/env python3
"""Exibe relatorio de criancas por atividade.

imprimir a lista de criancas agrupadas por sala
que frequentao cada uma das atividades.
"""

__version__  = "0.1.1" 

#Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos","Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Ingles", aula_ingles),
    ("Musica", aula_musica),
    ("Danca", aula_danca),
]

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:
    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

    #sala1 que tem intersecao com atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(atividade)

    print("sala1 ", atividade_sala1)
    print("sala2 ", atividade_sala2)

    print()
    print("#" * 40)
    
