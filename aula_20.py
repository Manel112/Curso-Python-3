# valor_1 = input('Digite o primeiro valor ')
# valor_2 = input('Digite o segundo valor ')

# if valor_1 > valor_2:
#     print('O valor "1":', valor_1, 'é maior que o valor "2": ', valor_2)
# elif valor_1 == valor_2:
#     print('O valor "1": ', valor_1, 'é igual ao valor "2" ', valor_2)
# elif valor_2 > valor_1:
#     print('O valor "2"', valor_2, 'é maior que o valor "1"', valor_1)


#outra forma de fazermos é usand o fstring, que eu não usei na primeira vez que fiz o exercício
valor_1 = input('Digite o primeiro valor ')
valor_2 = input('Digite o segundo valor ')

if valor_1 >= valor_2:
    print(f'{valor_1=} é maior ou igual ao {valor_2=}')

else:
    print(f'{valor_2=} é maior ou igual do que {valor_1}')
