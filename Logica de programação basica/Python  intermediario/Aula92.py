# Generator expression, Iterables e Iterators em Python
# funcoes que sabem pausar em determinada ocasião
# não tem tamanho, não tem indice, pois não esta na memória

import sys

iterable = ["Eu", "Tenho", "__iter__"]
iterator = iterable.__iter__() # tem __iter__ e __next__

lista = [n for n in range(100)]
generator = (n for n in range(100)) # o generator é feito com () parenteses

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))

