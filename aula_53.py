# enumerate - enumera os iteraveis

lista = ['Emanuel', 'Maria', 'João']
lista.append('Pedro')

for indice, nome in enumerate(lista):
    print(indice, nome)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')