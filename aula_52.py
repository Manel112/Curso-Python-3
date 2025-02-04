#Tipo tupla - uma lista imutavel
#tupla é uma lista que não pode ser alterada

nomes = 'Maria', 'Luiz', 'Emanuel'
#nomes = tuple(nomes), transforma a variavel em uma tuple
#nomes = list(nomes), transforma a variavel em uma lista
print(nomes) #caso tentemos alterar ela com os comandos de lista, da erro
print(nomes[-1])