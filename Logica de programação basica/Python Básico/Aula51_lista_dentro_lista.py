"""
Lista de listas e seus indices
"""
salas = [
    # 0           1
    ["Maria", "Helena", ],  # 0 (indice)
    # 0 
    ["Elaine", ], # 1 (indice)
    # 0           1           2
    ["Luiz", "João", "Eduarda"], # (0,10, 20, 30, 40)], # 2 (indice)
]

# print(salas[0][1])
# print(salas[1][0])
# print(salas[2][2])
# print(salas[2][3][2]) # modo de busca entre as listas


for sala in salas: # o for maior faz a primeira lista ("salas")
    print(f"A sala é {sala}") # o for menor ira fazer a lista de dentro("alunos")
    for aluno in sala:
        print(aluno)
