"""
Valores padrão para parametros
Ao definir uma função, os parâmetros podem ter valores padrão
Caso o valor não seja enviado para o paramêtro, o valor padrão será usado
Refatorar: editar seu código antigo
"""

def soma (x, y, z=None): #z=None é o valor padrão
    if z is not None: 
        print(f'{x=}, {y=}, {z=}', '|','x + y + z =', x + y + z)
    else:
        print(f'{x=}, {y=}', '|', 'x + y =', x + y)

soma(1, 3)
soma(1, 5, 0)
soma(1, 10, 10)