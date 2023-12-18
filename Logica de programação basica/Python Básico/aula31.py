""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else: # o else encerra o while, porem se houver um break antes ele não é executado
    print('Não encontrei um espaço na string.')
print('Fora do while.')

