""" 
Exercicio
Exiba os indices da lista
"""

lista = ['Pedro', 'Leonardo', 'Rafael', 'Guilherme']

lista.append ("Lucas")

indices = range(len(lista))

for indice in indices:

    print(indice, lista[indice], type(lista[indice]))