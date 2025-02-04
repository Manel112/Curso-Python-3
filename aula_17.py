#Apenas revisão da aula 16
#porem, nós temos agora a informação de que:
#os if e elif serão executados em ordem, de forma que
#se a primeira e a segunda condição forem satisfeitas, será mostrado apenas a primeira
#e assim por diante

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('A condição 1 é verdadeira')
elif condicao2:
    print('A condição 2 é verdadeira')
elif condicao3:
    print('A condicao 3 é verdadeira')
elif condicao4:
    print('A condição 4 é verdadeira')
else:
    print('Nenhuma das condições é verdadeira')