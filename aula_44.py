"""
For + Range
o range é definido em start, stop e step.
quando colocamos 1 número, ele sera o numero de stop
se colocamos um começo e um fim, é o start e o stop
e o ultimo é de quanto em quanto ele vai dar o passo, por exemplo:
range(0,10,2), ou seja, ele começa no 0, vai até o 10 de 2 em 2
"""

numeros = range(0,10,2)  #pode ser feito também com números negativos

for numero in numeros:
    print(numero)