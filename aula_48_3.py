"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
lista.append('Emanuel')
nome = lista.pop()
lista.append(321321839)
del lista[-1] #-1 sempre vai ser o ultimo item da lista
#lista.clear() limpa a lista
lista.insert(0, 5) #primeiro argumento seleciona o indice, segundo argumento o que vc quer escrever
print(lista)