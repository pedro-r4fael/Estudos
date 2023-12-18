# Dictionary Comprehension e Set Comprehension

produto = {
    "Nome": "Caneta Azul",
    "preco": 2.5,
    "categoria": "Escritório",
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor 
    in produto.items()

}


s1 = {2 ** i for i in range(10)}

print(dc)
print(s1)