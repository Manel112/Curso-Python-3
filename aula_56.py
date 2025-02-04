"""
split e join com lista e str
split - divide a lista ou a str
join - une a string
"""

frase = 'Emanuel foi comprar pão, mas voltou sem o pão'
lista_frases_crua = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_crua):
    lista_frases.append(lista_frases_crua[i].strip()) #.strip corta os espaços do final e do começo

print(lista_frases_crua)
print(lista_frases)

frase2 = ['Emanuel foi comprar pão', 'mas voltou sem o pão']
frase_unida = ', '.join(frase2)
print(frase_unida)
