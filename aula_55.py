#Imprecisão do ponto flutuante
import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2

print(numero_3) #não está arredondado
print(f'{numero_3:.2f}') #arredonda pra duas casas decimais, retorna string
print(round(numero_3, 2)) #retorna 2 casas decimais, porem retorna um float

