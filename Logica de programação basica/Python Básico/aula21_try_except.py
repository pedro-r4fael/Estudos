
numero_str = input("vou dobrar o numero digitado ")

# print(numero_str.isdigit())

# if numero_str.isdigit():
   

try:
    print("STR",numero_str)
    numero_float = float(numero_str)
    print("FLOAT:", numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2:.1f}")
    

except:
    print("Digite um numero para ser valido")


