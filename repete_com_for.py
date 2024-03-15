#!/usr/bin/env python3

# numbers = [1, 2, 3, 4, 5, 6]
numbers = range(1, 11)

# Iterable
"""
for number in nymbers:
    par = number % 2 == 0
    if par:
        print(number)
    else:
        continue

    print(f"mais codigo com {number}")


for line in  open("post.txt"):
    if line == "---\n":
        break
    print(line)


dados = {}
for line in  open("post.txt"):
    if line == "---\n":
        break
    key, valor = line.split(":")
    dados[key] = valor.strip()

print(dados)

"""
# for loops / laco for
original = [1, 2, 3]
dobrado = []
for n in original:
    dobrado.append(n * 2)

print(dobrado)

# Funcional
# List Comprehension
dobrado = [n * 2 for n in original]
print(dobrado)


# Dict comprehension
dados = {
    line.split(":")[0]: line.split(":")[1].strip()
    for line in open("post.txt") 
    if ":" in line }
print(dados)
