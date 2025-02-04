"""
Interpolação de strings
para fazer isso, é como se fosse o f-string que já fizemos, porem
nós usamos o % para sugerir o que queremos substituir
%s = string
%d, e, ou i, = int
%f = float
para usarmos os hexas decimais, também podemos fazer com 
%x (para minusculo) e %X (para maiúsculo)
"""

nome = 'Emanuel'
preco = 299.99
variavel = '%s, o preço em R$ é %.2f ' % (nome, preco)
print(variavel)

#para usar o hexadecimal nós usamos:
print('O hexadecimal é %x' %(14)) 
#tem que colocar um parenteses depois da % do hexadecimal