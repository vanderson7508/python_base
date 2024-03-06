#!/usr/bin/env python3
"""Exibe relatorio de criancas por atividades

imprimir a lista de cruancas agrupadas por
sala que frequenta cada uma das atividades.



__version__ = "0.1.0"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles =  ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

#listar alunas em cada atividade por sala

aula_ingles_sala1 = []
aula_ingles_sala2 = []

for aluno in aula_ingles:
    if aluno in sala1:
        aula_ingles_sala1.append(aluno)
    elif aluno in sala2:
         aula_ingles_sala2.append(aluno)

print("Ingles sala1", aula_ingles_sala1)
print("Ingles sala2",aula_ingles_sala2)

aula_musica_sala1 = []
aula_musica_sala2 = []

for aluno in aula_musica:
    if aluno in sala1:
        aula_musica_sala1.append(aluno)
    elif aluno in sala2:
         aula_musica_sala2.append(aluno)


print("Musica sala1", aula_musica_sala1)
print("Musica sala2",aula_musica_sala2)

aula_danca_sala1 = []
aula_danca_sala2 = []

for aluno in aula_danca:
    if aluno in sala1:
        aula_danca_sala1.append(aluno)
    elif aluno in sala2:
         aula_danca_sala2.append(aluno)


print("danca sala1", aula_danca_sala1)
print("danca sala2",aula_danca_sala2)

"""

__version__ = "0.1.0"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles =  ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Ingles",aula_ingles),
    ("Musica",aula_musica),
    ("Dança",aula_danca)
]

#listar alunas em cada atividade por sala

for nome_atividade,  atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40 )

    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print("sala1 ", atividade_sala1)
    print("sala2 ", atividade_sala2)
    print()
    print("#" * 40)
