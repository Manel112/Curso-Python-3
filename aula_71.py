"""
args: Argumentos não nomeados
*args (empacotamento e desempacotamento)
igualmente quando faziamos para desempacotar os dados, com o *resto, ou *_, podemos fazer isso
com os argumentos da função
assim, a função aceitará quantos valores você colocar nela e não dará erro.
"""

x, y, *resto = 1, 2, 3, 4, 5
print(x, y, resto)

def soma(*args): #aceita quantos argumentos nós quisermos 
    total = 0
    for numero in args:
        print('Total', total, numero)
        total = total + numero
        print('Total', total)
    print(total)

soma(1,2,3,4,5,6)

soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros)) #faz a mesma ideia da soma que definimos
# print(*numeros)