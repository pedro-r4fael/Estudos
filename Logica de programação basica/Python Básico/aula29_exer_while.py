"""
iterando strings com while
"""

#      123456789101112
nome = "Pedro Rafael" #Iteraveis
#      121110987654321

tamanho_nome = len(nome)



# print(nome)
# print(tamanho_nome)
# print(nome[3])


indice = 0
novo_nome = ""
while indice < len(nome):
    letra = nome[indice]
    novo_nome += letra
    indice += 1
 
print(novo_nome) #pega letra e soma com letra pra formar o "nome" final.


#while é utilizado para coisas que sao variais, sem saber das repetiçoes