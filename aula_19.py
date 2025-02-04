"""
Operadores de comparação
O       Significado     Exemplo
>       maior           2 > 1
>=      maior ou igual  2 >= 2
<       menor           1 < 2
<=      menor ou igual  2 <= 2
==      igual           'a' == 'a'
!=      diferente       'a' != 'b'
"""

maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
formato = 'Essas são as condições: {}, {}, {}, {}, {}, {}'.format(maior, 
maior_ou_igual, menor, menor_ou_igual, igual, diferente)
print(formato)