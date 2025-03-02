#map, partial, GeneratorType e esgotamento de Iterators
#o map ele vai fazer o que nós faziamos em list comprehension
#porem, de uma forma mais simples, recebendo uma função, no 1o argumento e um parâmetro no 2o

from functools import partial
from types import GeneratorType

#map - serve para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

auemntar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)
#partial serve para fazer de uma maneira mais simples, o list comprehension para
#aumentarmos o produto em 10%

# novos_produtos = [
#     {**p, 'preco': auemntar_dez_porcento(p['preco'])} for p in produtos
# ]

def muda_preco_de_produtos(produto):
    return  {**produto, 
                'preco': auemntar_dez_porcento(produto['preco'])}

novos_produtos = list(map(muda_preco_de_produtos, produtos))

print_iter(produtos)
print_iter(novos_produtos)

print(list(map(lambda x: x * 3, [1,2,3,4])))
#no caso acima, conseguimos ver melhor, que o map recebe uma função, lambda
# e um argumento, que no caso foi a lista, [1,2,3,4]