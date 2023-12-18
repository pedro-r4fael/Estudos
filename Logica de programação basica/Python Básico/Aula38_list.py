"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4 #indices
#       -5   -4     -3             -2   -1 
lista = [123, True, 'Luiz Otávio',  1.2, []] # Suporta vários valores de qualquer tipo
lista[2] = 'Pedro'
print(lista)
print(lista[2], type(lista[2]))