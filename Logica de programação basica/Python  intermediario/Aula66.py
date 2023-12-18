"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z): # Parametro vem na definição da função
    #definição

    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

    print(f"O valor da soma é {x + y + z}")

soma(1,2,3) # Argumento é o valor da variável # tomar cuidado com a ordem (é usado em sequencia)
soma(y=2, x=1, z=3) 

# print(soma(1,2)) # para fazer a função funcionar é necessário os parenteses
