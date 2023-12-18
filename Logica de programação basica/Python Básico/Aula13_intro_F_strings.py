nome = 'Pedro Gregório'
altura = 1.81
peso = 72
imc = peso / (altura * altura)
# print(nome,"tem", altura, "de altura, pesa", peso, "kg e seu IMC é",

#f-strigns (f de formatacao)
linha_1 = f"{nome}, tem {altura} de altura,"
linha_2 = f"pesa {peso} quilos e seu IMC é"
linha_3 = f"{imc: .2f}"

print(linha_1)
print(linha_2)
print(linha_3)
