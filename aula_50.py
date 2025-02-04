#for in com listas, já que ela é iteravel, o for funciona

lista = ['Joao', 'Emanuel', 'Maria']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))