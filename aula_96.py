#Yield from
#nós podemos fazer uma logica seguindo os generators de outras funções
#com o yield from, por exemplo:

def gen1():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

def gen2():
    yield from gen1()
    yield 6
    yield 7
    yield 8
    yield 9

g = gen2()
for numero in g:
    print(numero)