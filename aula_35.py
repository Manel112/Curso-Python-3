"""
Repetições
while (enquanto)
Executa uma ação enquanto a condição for verdadeira
Loop infinito: quando  um código nao tem fim
"""

condicao = True

while condicao:
    nome = input("Qual o seu nome: ")
    print(f'Seu nome é {nome}')

    if nome == 'sair':
     break  #quebra o while, após ele fazer as condições acima, o break quebra o while.

print (f'Acabou')