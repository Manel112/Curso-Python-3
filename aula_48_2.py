"""
Listas em Python
Tipo list - Mutável
Suporta valores de qualquer tipo
Da pra usar indice e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update Delete = lista[1] (CRUD)
"""

lista = [10, 20, 30, 40, 50]
# lista[2] = 300
# del lista[2] #como o 30 foi deletado, no print do indice 2 da lista, mostra o 40
# print(lista)   
# print(lista[2])
lista.append(60) #adiciona ao final da lista ".append"
lista.pop() #remove o ultimo item da lista ".pop", caso coloquemos o indice desejado, ele remove
            #apenas o indice que indicamos
print(lista)