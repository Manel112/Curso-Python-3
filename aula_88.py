#List comprehension em Python
#List comprehension é uma forma rápida para criar listas
#a partir de iteráveis

import pprint

def p(v):
    pprint.pprint(novos_produtos, sort_dicts=False, width=40)

lista = []
for numero in range(10):
    lista.append(numero)
#print(lista)

#podemos fazer a mesma coisa, dentro de uma lista com o list comprehension

lista = [numero for numero in range(10)] #podemos colocar a lógica dentro da lista, mas para
#isso, colocamos do lado esquerdo o que queremos fazer
# print(lista)

# lista = [
#     numero * 2
#     for numero in range(10)
# ]

# print(lista)

#Mapeamento de dados para list comprehension
produtos =[
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p3', 'preco': 10},
    {'nome': 'p2', 'preco': 30},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
#a nova lista do mapeamento, tem que ter o mesmo numero de caracteres q a lista antiga
#no mapeamento, o if vem antes do for
# print(*novos_produtos, sep='\n')


#no filtro, o if vem DEPOIS do for
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >=20 and produto['preco'] * 1.05) > 20
]

p(novos_produtos)