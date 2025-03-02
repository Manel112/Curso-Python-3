import json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

# with open('aula_119.json', 'w', encoding='utf8') as arquivo:
#     json.dump(pessoa, arquivo, ensure_ascii=False, indent=2) 
# serve para jogar as coisas dentro do aqruivo que estamos criando

with open('aula_119.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])
#o json.load, serve para carregar os dados da base de dados json que nós queremos
#ou seja, vc pega os dados de uma base que ja existe.