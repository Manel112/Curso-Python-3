#Manipulando chaves e valores em dicionários no Python
#podemos manipular o valor das chaves e fazer o CRUD com elas, tal qual como listas
pessoa = {}

chave = 'nome'
pessoa[chave] = 'Emanuel Lucas'
pessoa['sobrenome'] = 'Alves de Souza'

print(pessoa[chave])

pessoa[chave] = 'Larissa' #dicionarios são mutaveis, posso alterar o valor depois
print(pessoa)

del pessoa['sobrenome']

if pessoa.get('sobrenome') is None: #.get, usa para tentar pegar o nome e não dá Key Error
    print('Não Existe')
else:
    print(pessoa['sobrenome'])

