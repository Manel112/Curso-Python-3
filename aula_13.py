#existe uma função chamada de f-string, onde nós podemos colocar variaveis no meio da string
#nós fazemos isso criando uma variavel para a string e colocando um "f" antes da string
#de modo que, para chamarmos aquilo dentro da string de variavel, é necessario envolver
#a variavel entre chaves

#para colocarmos a quantidade de casa decimal que queremos, nós usamos o comando
#:.Xf e em seguida, colocamos o numero de casa decimal que queremos
#substituimos o X pelo numero de casas
#por exemplo :.2f (duas casas decimais)




nome = 'Emanuel Lucas Alves de Souza'
altura = float (1.78)
peso = float (71.0)
imc = peso / (altura * altura) #IMC = peso / (altura * altura)
linha_1 = f'{nome}, tem, {altura}, de altura e pesa, {peso}, kilos e seu IMC é {imc:.2f}'

print (linha_1)


