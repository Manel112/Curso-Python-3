"""O segundo operador lógico é o operador 'or'
ele funciona como uma especie de soma dos operadores lógicos
ou seja, se tiver alguma coisa verdadeira, ou true, na expressão, ele vai retornar true
Exemplo: (0 or false or 0 or True), ele retornará o True.
nós usamos ele apenas digitand o comando 'or', da mesma forma que usamos o and
Nesse código, só vai funcionar caso usemos o 'E' maiúsculo, para que funcione com outras letras
ou o e minusculo, usamos o comando or.
E para que façamos a entrada ler primeiro, somente o E ou o e, nós vamos colocar entre parenteses
como uma expressão matematica
"""

entrada = input("[E]ntrar ou [S]air: ")

senha_digitada = input("Digite sua senha: ")
senha_permitida = "123456"

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print ("Você entrou.")
else:
    print ("Você saiu")