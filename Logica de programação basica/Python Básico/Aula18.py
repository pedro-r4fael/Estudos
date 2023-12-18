
entrada = input("[E]ntrar [S]air ")

senha_digitada = input("Senha: ")

if entrada == "S":
    print("Sair!")
senha_permitida = "123456"

if entrada == 'E' or 'e' and senha_digitada == senha_permitida:
    print("entrou")

else:
    print("Acesso negado!")
