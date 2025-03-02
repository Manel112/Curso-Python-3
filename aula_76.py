# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

pessoa = {
    'Nome': 'Emanuel Lucas', #type, dict, é um dicionario, conseguimos acessar
    'Sobrenome': 'Alves de Souza', #as informações através dos indices que nós damos
    'Idade': 23, #diferentemente da lista, onde os indices começam do 0
    'Altura': 1.8, 
    'Endereços': [
        {'Rua': 'não sei o que da silva', 'numero': 182},
        {'Rua': 'não sei o que da costa', 'numero': 220}, 
        ]
    
}

# print(pessoa, type(pessoa))
print(pessoa['Altura']) #assim, acessamos o indice que quisermos

#tambem conseguimos separar as chaves com o for

for chaves in pessoa:
    print(chaves, pessoa[chaves])



