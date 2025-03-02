# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(lista1, lista2):
#     intervalo = min(len(lista1), len(lista2))
#     return [
#         (lista1[i], lista2[i]) for i in range(intervalo)
#     ]

# lista1= ['Salvador', 'Ubatuba', 'Belo Horizonte']
# lista2= ['BA', 'SP', 'MG', 'RJ']
# print(zipper(lista1, lista2)), assim, fazemos uma funçao zipper
#porem, o python já tem uma propria função zipper, que usamos dessa forma:

lista1= ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2= ['BA', 'SP', 'MG', 'RJ']
print(list(zip(lista1, lista2))) #faz o dalista menor, com a maior

#porem, tambem existe o contrario, usando um import

from itertools import zip_longest
lista1= ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2= ['BA', 'SP', 'MG', 'RJ']
# print(list(zip_longest(lista1, lista2)))
#podemos preencher o none, adicionanod um fill value

print(list(zip_longest(lista1, lista2, fillvalue= 'SEM CIDADE')))