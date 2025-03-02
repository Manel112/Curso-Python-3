def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador): 
    def multiplica(numero):
        return numero * multiplicador
    return multiplica 
#o lambda poderia ser utilizado aqui, mas como não é simples, é melhor definir mesmo a função
#pois fica complexo e mais difícil de ler o código.

duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))

#lambda é repetido muitas vezes e fica difícil de entender o que foi feito

print(
        executa(
        lambda x, y: x + y,
        2, 3 #não precisa dos () para definir os parametros e usa : para os argumentos
        ),
        executa(soma, 2, 3), #mesma coisa que usar o lamda
        soma(2,3) #mesma coisa
     )

print(
    executa(
        lambda *args: sum(args),
        1,2,3,4,5,6,7,8,9
    )
)