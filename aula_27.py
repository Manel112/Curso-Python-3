"""
Fatiamento de string
o fatiamento de string serve, como o nome sugere, fatiar as strings que a gente quer
por exemplo, se queremos saber a quarta letra de uma string, nós podemos usar o fatiamento
para a string de exemplo:
 0 1 2 3 4 5 6
 E m a n u e l
-7-6-5-4-3-2-1
Para usar o fatiamento, nós vamos ter o [i:f:p]
onde o i significa o inicio
f significa o fim
e p significa o passo, ou seja, de quanto em quanto vamos fatiar
caso deixamos em branco o inicio, o programa entende que deve começar no inicio,
caso omitimos o f, o programa entende que é para ir até o final.
para usarmos o fatiamento, nós vamos inserir o comenado entre colchetes, como mostra ali em cima
outra função interessante é a função len, que da pra gente o numero de caracteres na string
que estamos olhando, na string de exemplos, nós temos 7 caracteres (contamos o 0)
"""
variavel = 'Emanuel'
print(variavel[0:1]) #mostra o primeiro caractere
print(variavel[:7:2]) #mostra os sete caracteres de dois em dois
print(variavel[::3]) #mostra os caracteres do inicio ao final, de tres em tres
print(len(variavel)) #a função len mostra o numero de caracteres
print(variavel[::-1]) #conta os caracteres de tras para frente, pois o passo está em -1