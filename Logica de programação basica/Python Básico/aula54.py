"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
# condicao = 10 == 10
# variavel = "Valor" if condicao else "Outro valor"

# print(variavel)

digito =  2 # > 9 = 0

# se o digito dor maior do que 9 ele sera igual a 0, se for menor tera o msm valor
novo_digito = digito if digito <= 9 else 0 
print(novo_digito)