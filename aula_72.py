# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicador(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
        
multiplicacao = multiplicador(1, 5, 15)
print(multiplicacao)

#Crie uma função que fala se um número é par ou impar
#Retorne se o número é par ou impar

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois is True:
        return f'{numero} é par.'
    return f'{numero} é impar' #um else aqui é redundante, não precisa ser usado

print(par_impar(2))
print(par_impar(4))
print(par_impar(5))
print(par_impar(10))
print(par_impar(15))
