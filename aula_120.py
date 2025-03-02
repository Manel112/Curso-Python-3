#Problema dos parâmetros mutáveis em python
#ao invés de eu chamar direto na definição da função um parâmetro mutável
#é melhor que eu chame ela no corpo da função, para que ela sempre seja executada
#e execute de forma individual, caso contrário, se eu chamo ela logo quando formos definir
#a função, ela vai funcionar de uma forma conjunta, como se fosse apenas um parâmetro mutável

def adiciona_clientes(cliente, lista=None):
    if lista is None:
        lista = []
    lista.append(cliente)
    return lista

cliente1 = adiciona_clientes('João')
adiciona_clientes('Maria', cliente1)
adiciona_clientes('Emanuel', cliente1)
adiciona_clientes('Pedro', cliente1) #preciso colocar em qual lista eu desejo adicionar o valor
print(cliente1)

cliente2 = adiciona_clientes('Larissa')
adiciona_clientes('Emanuel', cliente2)
print(cliente2)