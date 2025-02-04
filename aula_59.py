#Desempacotamento em chamadas
#de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Emanuel', 1, 2, 3, 4, 'Lucas']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# a, b, *_, ap, u  = lista
# print(b, u, ap )

#for nome in lista:
   # print(nome)  #para fazermos isso, sem precisarmos usar o for, nos usamos um * antes da variavel

print(*string) 
print(*lista, sep='\n')
print(*tupla, sep=' ')
print(*salas, sep='\n')