"""
Closure e funções que retomam outras funções
"""
def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar # sem os parenteses de execução ele apenas guarda forçadamente o valor na "memória" ate que ele seja executado com "()" em qualquer linha do codigo

falar_bom_dia = criar_saudacao("Bom dia")
falar_boa_tarde = criar_saudacao("Boa tarde")

print(falar_bom_dia("Pedro")) # os parenteses na frente de s1 definem o fechamento para executar o saudar do primeiro retorno
print(falar_boa_tarde("Pedro")) # o closure seria o fechamento, que estava em memoria ate ser executado com "()" aqui

for nome in ["Pedro", "Leonardo", "Guilherme", "Rafael"]:
    print(falar_bom_dia(nome))
    print(falar_boa_tarde(nome))