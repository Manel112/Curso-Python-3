"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input("Digite um número inteiro: ")

try:
    if numero:
        int_numero = int(numero)
    if (int_numero % 2) == 0:
        print(f"O número {int_numero} é par")
    elif (int_numero % 2 ) != 0:
        print(f"O número {int_numero} é impar")   
except:
    print("Você não digitou um numero inteiro")

