import json

# from pathlib import Path

# caminho_projeto = Path()
# print(caminho_projeto.absolute())

# caminho_arquivo = Path(__file__)
# print(caminho_projeto)


# print(caminho_arquivo.parent)


# puxa o arquivo direto do diretorio colocado e o carrega na variavel "projeto"
with open("/home/wilson/estudos/projeto/Logica de programação basica/Python  intermediario/Aula_teste.json", "r") as arquivo:
    projeto = json.load(arquivo)

print(projeto)