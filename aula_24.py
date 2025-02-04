"""
Outro operador lógico é o in ou o not in
o in ele serve para ver se aquilo que você pediu está ali dentro
por exemplo
no nome Emanuel, nós usaremos o in para checar se tem o que nós queremos
dentro desse nome, por exeplo, se existe a letra a no nome emanuel, o in checa isso.

 0 1 2 3 4 5 6
 E m a n u e l
-7-6-5-4-3-2-1
"""


nome = 'Emanuel Lucas'

print(nome[0]) #uma maneira de checar o in de modo "manual" seria pedindo o print para
               #imprimir a letra especifica
print(nome[-3])
print(20 * '-')

#porem, um outro jeit oque temos de imprimir a mesma coisa é usand o comando in

print('nu' in nome) #como tem nu em Emanuel, ele retorna True
print(' ' in nome) #como não tem pereca em Emanuel, ele retorna False.