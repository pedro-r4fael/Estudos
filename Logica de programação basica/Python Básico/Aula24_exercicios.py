"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


numero_digitado = input("digite um numero inteiro ")


if numero_digitado.isdigit():
    ...
    numero_int = int(numero_digitado)
    par_impar = numero_int % 2 == 0
    par_impar_text = "ímpar"
    
    if par_impar:
        par_impar_text = "par"



    print(f"o numero {numero_int} é {par_impar_text}")

else:
    print("voce não digitou um numero inteiro")



hora_digitada = input("Qual é a hora em numeros inteiros? ")



try:
    hora_int = int(hora_digitada)
    if hora_int >= 0 and hora_int <= 11:
        print("Bom dia!")
    elif hora_int >= 12 and hora_int <= 17:
        print("Boa tarde!")
    elif hora_int >= 18 and hora_int <23:
        print("Boa noite!")
    else:
        print("Não conheço essa hora")


except:
    print("por favor digite numeros inteiros")


primeiro_nome = input("Digite seu primeiro nome ")

letras_nome = len(primeiro_nome)
try:
    if letras_nome <= 4:
        print("seu nome é muito curto")
    elif letras_nome == 5 and 6:
        print("seu nome é normal")
    else:
        print("seu nome é muito grande")

except:
    print("digite mais que uma letra")










