"""
F-strings
para usarmos as f-strings, vamos fazer igual nós fizemos na outra aula que falamos de f strings
vamos usar um f, antes da string
Ex:
print(f'blablabla')
para as formatações da string, nós temos:
s - para string
d - para int
f - para float
x ou X para o hexadecimal
e nós podemos incluir caracteres na esquerda, na direita, ou colocar nossa string no centro
para isso, nós usamos o sinal de
> (para colocar caracteres na esquerda)
< (para colocar caracteres na direita)
^ (para colocar os caraceteres no meio)
para colocar o sinal de mais ou menos, nós usamos (- ou +)
existem algumas conversions flags (não sei o que é)
que são: !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:->10}') #colocamos os 2 pontos e para onde queremos os caracteres
print(f'{variavel:-<10}')
print(f'{variavel:-^10}')
print(f'O hexadecimal de 15 é {15:x}')
print(f'{1500.1209312903123:,.2f}') #a vírgula antes do .2f serve para colocar a "," 
                                    #para marcar o mil.