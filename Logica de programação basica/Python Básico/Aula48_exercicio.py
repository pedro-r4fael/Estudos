"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores em sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista
"""

# inserir = "i"
# apagar = "a"
# listar = "l"
# letras_validas = "i", "a", "l"


# while True:
#     print("Selecione uma opção") 
#     letra_digitada = input ("[i]nserir [a]pagar [l]istar: ")

    

#     for letra_digitada in letras_validas:
#         if letra_digitada == inserir:
# 
#             produto_digitado = input("Digite o produto: ")
            
#             lista = range(len(produto_digitado))
#             for item in lista:
#                 print(item, lista)
#         if letra_digitada == apagar
            
            

# else:
#     print("Digite uma opção valida, tente novamente!")


### ### correção

import os # importar opção para limpar o terminal


lista = [] #lista aonde sera utilizado como diretorio

while True:
    print("Selecione uma opção") 
    opcao = input("[i]nserir [a]pagar [l]istar: ")
    
    if opcao == "i":
        os.system("clear") # limpa console antes de printar o comando
        valor = input ("Valor: ") #valor digitado pelo usuario
        lista.append(valor) # adiciona o valor digitado na lista principal

    elif opcao == "a":
        os.system("clear") #limpa console
        indice_str = input("Escolha um indice para apagar: ") # captura o numero digitado pelo usuario em string

        try:
           indice = int(indice_str) # transforma o numero string em inteiro
           del lista[indice] #deleta o item no indice numerico selecionado
        except ValueError:
            print("Não foi possivel apagar esse indice")
        except IndexError:
            print("Indice não existe na lista")


    elif opcao == "l":
        os.system("clear") # limpa console
        
        if len(lista) == 0:
            print("Nada para listar")

        for i, valor in enumerate(lista): 

            print(i, valor) # mostra o indice crescente e os valores colocados na lista pelo usuario





    else: # Else de erro principal
        print("Por favor escolha i, a ou l") 
