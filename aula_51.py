#Introdução ao desempacotamento
# nome1, nome2, nome3 = ['Emanuel', 'Maria', 'João']
# print(nome2)  #podemos separar os valores dentro da lista com diferentes variaveis

#porem, caso queiramos imprimir apenas um valor, podemos usar o *resto, o * guarda o valor
#dentro de uma lista separada

nome1, *_ = ['Emanuel', 'Maria', 'João']
print(nome1)#caso imprimamos o *_, aparecera a lista
            #porem, para nós guardarmos a lista com os outros nomes, é comum que usemos _
            #para representar que ali tem uma variavel que nao vamos usar, logo, *_