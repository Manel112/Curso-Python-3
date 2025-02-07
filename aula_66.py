"""
Argumentos nomeados e não nomeados
O argumento nomeado ele recebe o nome da variavel
O argumento não nomeado, ele nã orecebe o nome da variavél
"""

def soma(x,y):
    print(f'{x=}, y={y}', '|', 'x + y = ', x + y)

soma(x=1, y=2) #argumento nomeado x=1, y=2
soma(5, 6) #argumento não nomeado, ou argumento posicional
#obs: vc não pode enviar argumentos posicionais, depois de argumentos nomeados