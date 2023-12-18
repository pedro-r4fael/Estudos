# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

d1 = {
    "c1": 1,
    "c2": 2,
}

d2 = d1() #copia rasa, nao copia listas e outros dentro da chave
# d2 = copy.deepcopy(d1) #copia profunda de todas as linhas

d2["c1"] =  100
print(d1)
print(d2)
