"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Pedro', 'Maria', 1, True, 1.2]
# lista_b = lista_a # esta apenas direcionando a lista, o valor é o mesmo para as duas listas.
lista_b = lista_a.copy() # esta copiando a lista a.

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
