lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y)) # a tupla dentro dos parenteses faz o papel de dado que suporta "2 indices juntos" na lista

lista2 = [
    (x,y)
    for x in range(3)
    for y in range(3)
]

print(lista)
print()
print(lista2)
