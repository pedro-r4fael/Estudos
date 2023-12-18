"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1 # x com valor global


def escopo():
    global x # o global puxa o x com o valor 1
    x = 10

    def outra_funcao():
        global x # usar o global para substituir o valor de x é uma má pratica de programação(pode ficar confuso)
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x) # pega o x sem estar dentro da função "escopo"
escopo() # pega os valores definidos dentro da função
print(x) # pega novamente o x sem estar dentro da função "escopo"