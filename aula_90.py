#Dictionary comprehension e set comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

# dc = {
#     chave: valor 
#     for chave, valor in lista
# }
# print(dict(dc))

s1 = {i for i in range(10)}
print(s1)

#mesma coisa que:
print(set(range(10)))