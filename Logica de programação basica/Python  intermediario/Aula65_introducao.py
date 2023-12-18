"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# def Print(): # define a função
#     print("Várias1")
#     print("Várias2")
#     print("Várias3")
#     print("Várias4")

def imprimir(a, b, c): # o que há dentro do parenteses é variavel
    print(a, b, c)
    

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)
# imprimir() # com parenteses vazio ele indica para inserir o valor 

def saudacao(nome="Sem nome"):
    print(f"Olá, {nome}!")

saudacao("Pedro")
saudacao("Leonardo")
saudacao("Guilherme")
saudacao("Rafael")
saudacao()
