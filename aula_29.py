"""
try e except
o try/except vai funcionar como se fosse um if/else
de modo que, o try vai tentar executar o código
e o except vai rodar caso dê algum erro no código
a diferença é que, no if, se a condição não bater, ele vai direto pro else, já no try
ele vai tentar fazer todas as linhas de código e na linha que der erro, ele vai pro except.
"""

numero_str = input("Vou dobrar o número que você digitar: ")

try:
    numero_float = float(numero_str)
    print(f'FLOAT: {numero_float}')
    print(f'O dobro do número {numero_str} é: {numero_float * 2}')
except:
    print(f'Você não digitou um número')

#o que acontece é que, se eu tivesse algo no try para receber uma STR
#primeiro ele daria print da string, depois que notasse que não é um número
#ele passaria para o except
