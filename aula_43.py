""" for/in, outro laço de repetição
nós usamos o while, quando não sabemos o numero de repetiçoes
que vamos ter, já no for, nós usamos para iterar algo que sabemos quantas repetições vao ter"""

texto = 'Emanuel'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')


