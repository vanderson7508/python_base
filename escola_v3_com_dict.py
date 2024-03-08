#!/usr/bin/env python3
"""Exibe relatorio de criancas por atividade.

imprimir a lista de criancas agrupadas por sala
que frequentao cada uma das atividades.
"""

__version__  = "0.1.2" 


#Dados
salas = {
    "sala1": ("Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"),
    "sala2":("Joao", "Antonio", "Carlos", "Maria", "Isolda"),
}
Aulas = {
    "ingles": ("Erik", "Maia", "Joana", "Carlos", "Antonio"),
    "musica": ("Erik", "Carlos","Maria"),
    "danca": ("Gustavo", "Sofia", "Joana", "Antonio"),
}
atividades = {
    "ingles": Aulas["ingles"],
    "musica": Aulas["musica"],
    "danca": Aulas["danca"],
}
# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades.items():
    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

   # sala1 que tem intersecao com atividade
    atividade_sala1 = set(salas["sala1"]) & set(atividade)
    atividade_sala2 = set(salas["sala2"]).intersection(atividade)

    print("sala1 ", atividade_sala1)
    print("sala2 ", atividade_sala2)
    print()
    print("#" * 40)
