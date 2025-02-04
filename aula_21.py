"""
Operadores Lógicos
para os operadores logicos, nós temos 3 tipos de operadores diferentes
o and, o or e o not.
para essa aula, vamos fazer o operador AND, ou "e".
para usarmos a funçao AND, usamos apenas o comando "and"
o and funciona como uma especie de multiplicação, logo, se algo na expressão for
falsy, a expressão inteira sera dada como falsa
por exemplo, True, True, True e False, gerará um false.
Alguns tipos de falsy que nos conhecemos são:
0, 0.0 e '' (string vazia sem espaço)
Também existe o "none" que é usado para representar um não valor. 
"""

entrada = input("[E]ntrar ou [S]air: ")

senha_digitada = input("Digite sua senha: ")
senha_permitida = "123456"

if entrada == 'E' and senha_digitada == senha_permitida:
    print ("Você entrou.")
    
#usamos o and para atrelar duas coisas ao mesmo tempo, ou seja, primeiro o programa
#vai conferir se foi digitado o 'E' ou o 'S' para entrar ou sair do programa
#depois vai conferir a senha digitada e se ela bate com a senha permitida
#após conferir essas duas coisas, ele dá a resposta dele

else:
    print ("Você saiu")