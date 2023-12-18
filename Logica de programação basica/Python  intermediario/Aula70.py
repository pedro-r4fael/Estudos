"""
Retorno de valores das funções (return)
"""
# return tem a função de retornar um valor para a função escolhida, pois a função exibe o valor mas equivale a NONE
def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y # se a condição de cima "if" não for válida essa será executada

soma1 = soma(2, 2)
soma2 = soma(3, 3)

# variavel = soma(1, 2)
# variavel = int("1")

print(soma1)
print(soma2)

print(soma(5, 55)) # ele faz a soma dos itens pois o primeiro valor é < 10
print(soma(11, 55)) # ele retorna o propio valor por é > 10
 