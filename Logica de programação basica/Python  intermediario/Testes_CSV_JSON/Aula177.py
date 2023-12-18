import json
import os

NOME_ARQUIVO = "aula177.json" #criando um caminho 
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

# dicionario
filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring', 

    'is_movie': True, 
    'imbd_rating': 8.8, 
    'year': 2001, 
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'], 
    'budget': None
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, "w") as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, "r") as arquivo:
    filme_do_json = json.load(arquivo) # tirou o s do load voce esta trabalhando com arquivo

print(filme_do_json)