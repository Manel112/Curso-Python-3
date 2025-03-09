# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

import enum

def mover(direcao):
    print(f'movendo para {direcao}')

#para o enum, para ficar mais organizado e mais legivel para outro dev, criamos uma classe
#e herdamos de enum, para que tenhamos um tipo.

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto() #enumera automaticamente
    DIREITA = enum.auto() 
    ACIMA  = enum.auto() 
    ABAIXO = enum.auto() 

print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA) #diferentes jeitos de chamar o enum
print(Direcoes(1).name, Direcoes.ESQUERDA.value) #name chama o nome da variavel
#value chama o valor

def mover(direcao: Direcoes): #faz com que o tipo de direção seja da classe direcoes
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção nao encontrada')
    
    print(f'movendo para {direcao.name} ({direcao.value})')

mover(Direcoes.ESQUERDA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)
mover(Direcoes.DIREITA)