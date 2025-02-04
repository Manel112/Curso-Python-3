"""
Listas em Python
Tipo list é mutavel, ou seja, a gente pode alterar ela depois de definida
as listas suportam valores de qualquer tipo, ex, int, bool, str, etc...
elas também podem ser visualizades pelos indices ([]) e fatiamento.
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

lista = [1.2, 'Emanuel', 123, True, []]  #quando colocamos [], estamos falando pro python que é uma lista
# print(lista), isso imprime a lista completa
lista[1] = 'Manelzin PvP' #alteramos o 2o item da lista que é emanuel, para outra coisa
print(lista[1].upper()) #imprime o segundo item da lista
print(lista, type(lista))
