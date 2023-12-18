"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#         1  2  3  4   #indices
lista = [10,20,30,40]

# lista[2] = 300 # substitui o valor do indice dentro da lista a partir dessa linha.
# del lista[2] # deleta o valor definido no indice.
# print(lista[2])

lista.append(50) # .append adiciona o valor no fim da lista
lista.pop() # remove o append anterior
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3) # ()vazio representa a ultima remocão.
                            # ()com o indice representa direto o indice para remoção.
print(lista,"Removido", ultimo_valor) 