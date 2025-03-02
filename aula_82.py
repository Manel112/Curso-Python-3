# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio
s1 = {'Emanuel', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# l1 = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5 , 5]
# s1 = set(l1) #tira os valores duplicados
# print(s1)
# l2 = list(s1)
# print(l2)
# for numero in s1:
#     print(numero) #também é iterável

# Métodos úteis:
# add, update, clear, discard
# s1 = set()
# s1.add('Emanuel') #adiciona no set
# s1.add(1) #adiciona no set
# s1.add(2) #adiciona um elemento set
# s1.update(('Gustavo', 1, 2, 3, 4, 5, 6,)) # deixa adicionar mais de um elemento no set
# s1.discard('Emanuel')
# s1.discard('Gustavo') # descarta o elemento que você colocou
# s1.clear() # limpa o set
# print(s1) 


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # união
s3 = s1 & s2 # intersecção
s3 = s1 - s2 # diferença
s3 = s1 ^ s2 #diferença simétrica
print(s3)