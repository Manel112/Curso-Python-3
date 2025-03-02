"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x,y in zip(lista_a, lista_b)]
print(lista_soma)

# for num1 in lista_a:
#     print(num1)
   
# print()
# for num2 in lista_b:
#     print(num2)


# lista_soma = list(zip(lista_a, lista_b))
# for valor1,valor2 in lista_soma:
#     soma = valor1 + valor2
#     print(soma)

