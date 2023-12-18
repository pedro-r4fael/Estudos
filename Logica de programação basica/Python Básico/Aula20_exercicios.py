# variavel = "Óla Mundo"


# print(variavel[-1:-10:-1])

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome} okay
        Seu nome invertido é {nome invertido} #okay
        Seu nome contém (ou não) espaços #okay
        Seu nome tem {n} letras #okay
        A primeira letra do seu nome é {letra} #okayas
        A última letra do seu nome é {letra} #okay
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios." #okay
"""


nome = (input ("digite seu nome "))
idade = (input("Digite sua idade "))

letras_nome = (len(nome))

if nome and idade:

    print(f"seu nome é {nome}")   
    print(f"o seu nome invertido é: {nome[::-1]}") #colocar codigo para inverter o nome

    if ' ' in nome:
    
        print("Seu nome contem espaços")
    
    else:
        print("Não contem espaços") 
        
    print(f"Seu nome tem {letras_nome} letras")
    
    print(f"A primeira letra do seu nome é:{nome[0]}")
        
    print(f"A ultima letra do seu nome é:{nome[-1]}")

else:
    
    print("Desculpe, você deixou campos vazios.")
    