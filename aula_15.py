#o comando "input", gera pra gente uma coleta de dados
#por exemplo, nós podemos usar o comando input para coletar algo que o
#usuario vai escrever

#nome = input('Digite o seu nome: ')
#print(nome)

#o input então, vai pedir pra o usuario dar os dados e podemos jogar esses dados em uma variavel
#da forma acima

#tambem podemos fazer isso para fazer operações aritiméticas, de modo que:

numero_1 = input('Digite um número ')
numero_2 = input('Digite o segundo número ')

numero_1_int = int(numero_1)
numero_2_int = int(numero_2)
print(f'A soma dos números é: {numero_1_int + numero_2_int}')

#porem, essa soma vai concatenar, já que a gente está chamadno os numeros de string, logo
#precisamos converter esse número para um int ou float
#para isso, criamos uma outra variavel para conversão