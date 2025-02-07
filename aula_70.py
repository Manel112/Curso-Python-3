# return serve para retornar o valor da função return()

def soma(x,y):
    if x > 10: #também posso colocar condições para o return
        return(2 * 5)
    return (x + y)
    #porém, o código acaba depois do return, não podemos colocar mais nada após ele

soma1= soma(2, 2)
soma2= soma(11, 3) #como x maior que 10, entra no if e retorna 2*5

print(soma1)
print(soma2)
print(soma1 + soma2)

def teste():
    print(1+1)
teste() #como não foi definido o que ele retorna, sempre vai retornar None
