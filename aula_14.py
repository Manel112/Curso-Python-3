#função formato, como o nome já sugre, ela formata as coisas
#nós podemos usar ela pra colocar coisas em ordem
#para formatar, envolvemos como em aspas como se fosse uma string
#e colocamos entre chaves e ele seguira a ordem
#para usar o comando, usamos .format

a = 'A'
b = 'B'
c = 2.5231

formato = 'a = {}, b = {}, c = {:.2f}'.format(a, b, c)

print(formato)

#tambem podemos nomear essas coisas, de modo que, se noemarmos o primeiro, precisamos nomear
#os outros, exemplo: formato = 'a = {}, b = {}, c = {:.2f}'.format(nome_1 = a, nome_2 = b,nome_ 3 = c)
#com isso, precisariamos colocar dentro das chaves
#nome_1, nome_2 e nome_3 respectivamente

