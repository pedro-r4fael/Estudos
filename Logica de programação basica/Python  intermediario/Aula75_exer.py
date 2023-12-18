# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplicar(*args):

#     for numero in args:
#         numero *= 2
#     return numero

# def triplicar(*args):

#     for numero in args:
#         numero *= 3
#     return numero

# def quadruplicar(*args):

#     for numero in args:
#         numero *= 4
#     return numero

# duplicacao = duplicar(5)
# triplicacao = triplicar(5)
# quadruplicacao = quadruplicar(5)

# print(duplicacao)
# print(triplicacao)
# print(quadruplicacao)

# Outra solução mais inteligente tambem poderia ser:

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))
