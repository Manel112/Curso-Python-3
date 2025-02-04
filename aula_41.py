""" while/else, no python existeo  else para o while, o que acontece é que, quando termina
o laço do while, o else será executado, porém, caso o while pare no meio, o else não será
executado"""

string = 'Qualquernome'

i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('O nome não tem espaço')
print('O else não foi executado')