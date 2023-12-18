# Manipulando chaves e valores em dicionários

pessoa = {}

##
##

chave = "nome"

pessoa[chave] = "Pedro Rafael"
pessoa["sobrenome"] = "Gregório"

print(pessoa[chave])

pessoa[chave] = "Maria"

del pessoa["sobrenome"] #deleta o "sobrenome" que se torna inexistente a partir dessa linha
print(pessoa)
print(pessoa["nome"])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')