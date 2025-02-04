"""
Repetições
while (enquanto)
Executa uma ação enquanto a condição for verdadeira
Loop infinito: quando  um código nao tem fim

funçao continue, vai continuar o laço, ou seja, vai fazer voltar no começo do if, while...
qualquer função que seja
"""

contador = 0

while contador <=100:
    contador += 1
    if contador == 10:
        
        print('Não vou mostrar o 10')
        continue  #Aqui, quando ele checar o 10, ele vai voltar no começo do while
    print(contador) #Ele fica dentro do while, para que ele some +1, cheque a condição do if e não imprima o 10
    if contador == 50:
        break
 
print('Acabou')