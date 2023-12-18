# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# print(list(range(10)))

import pprint

def p(v):
    pprint.pprint(novos_produtos, sort_dicts=False, width=40)

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
# print(lista)

# Mapeamento de dados em list comprehension

produtos = [
    {"nome": "p1", "preco": 20},
    {"nome": "p2", "preco": 10},
    {"nome": "p3", "preco": 30},
]

novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.05} 
    if produto["preco"] > 20 else {**produto}
    for produto in produtos
]

# print(novos_produtos)
# print(*novos_produtos, sep="\n") # sep= separa com quebra de linha

# Filtro
# o que vem na esquerda do For é mapeamento, e o que vem a direita é filtro

# p(novos_produtos) #esta definido como função em pprint

# lista = [n for n in range(10) if n < 5] # ele inclui o numero se a condição for verdadeira e não inclui no caso de ser falsa
# print(lista)

novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.05} 
    if produto["preco"] > 20 else {**produto}
    for produto in produtos
    if produto["preco"] > 10
]

p(novos_produtos)