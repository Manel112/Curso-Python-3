#Exercício
#Crie funções que duplicam, triplicam e quadriplicam o número recebido como parâmetro

# def duplicar(numero):
#     return numero * 2
# def triplicar (numero):
#     return numero * 3
# def quadriplicar(numero):
#     return numero * 4

# print(duplicar(20))
# print(triplicar(40))
# print(quadriplicar(40))

#Fazendo isso de uma forma mais simples

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(duplicar(4))
print(triplicar(4))
print(quadriplicar(4))