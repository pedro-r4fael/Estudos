"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

"""
"decimal" nao muito utilizado, porem util para quando for preciso calcular 
precisamente no fim de um numero de ponto flutante muito grande.
"""

import decimal 


numero_1 = decimal.Decimal ('0.1')
numero_2 = decimal.Decimal ('0.7')
numero_3 = numero_1 + numero_2

print(numero_3)
print(f'{numero_3:.2f}')

""" # round recebe o numero e voce define quantas casas decimais ele terá \
(continua em float, arredondando a casa decimal). """

print(round(numero_3, 3)) 



