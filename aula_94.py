#generator expression, iterables e iterators em python
import sys

iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable) #tem __iter__ e __next__, __iter__ é o iterator e __next__ é para pegarmos o próximo valor
lista = [n for n in range(1000000)] #guarda toda a lista na memória do computador
generator = (n for n in range(1000000)) #guarda apenas o generator na memória e não a lista toda
#além de ser uma funçao que pode PAUSAR.

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator) #pouca memória, porém só gera um por vez
#o diferencial é que, não podemos acessar o índice, por exemplo, podemos só pegar o proximo
#valor, e o proximo, e o proximo, diferentemente da lista, onde nós podemos pegar
#qualquer valor que quisermos, desde que usemos o índice

