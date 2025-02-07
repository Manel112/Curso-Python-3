"""
Introdução as funções (def) em Python
As funções vão servi como uma variável, porém, nos podemos definir um trecho de código
e não somente uma coisa só.
Elas podem receber os valores, e tambem os argumentos, entre os parênteses para
retornar um valor específico.
Por padrão, o Python retorna None (nada).
"""

def Print(): #definimos a função, agora toda vez que chamarmos ela, retornará o que esta dentro
    print('Arroz com Feijão')
    print('Arroz com Frango')

Print()

def imprimir(a, b, c): #parametros são definidos dentro do ()
    print(a,b,c)
imprimir(1,2,3) #quando chamamos a função, podemos mudar os parâmetros que demos pra ela
imprimir('João,', 'Maria e', 'Helena')