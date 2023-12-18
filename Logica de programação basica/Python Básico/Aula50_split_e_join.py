"""
split e join com list e str
split - divide uma string
join - une uma string 
"""

frase = "olha que, coisa interessante"

lista_de_palavras_cruas = frase.split(",") # split corta a frase no local que voce determina.

lista_de_palavras = []

for i, frase in enumerate(lista_de_palavras_cruas):
   
    # strip tem a função de cortar os espaços da frase (começo e fim)
    # lstrip (left), rstrip (right) 

    lista_de_palavras.append(lista_de_palavras_cruas[i].strip())


# print(lista_de_palavras_cruas) # contem os espaços.
# print(lista_de_palavras) # esta limpa e "formatada".

frases_unidas = "-".join(lista_de_palavras) # somente interavel (strings, listas e tuplas).

print(frases_unidas)
