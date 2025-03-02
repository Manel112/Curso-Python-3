#Combination - Ordem não importa
#Permutation - Ordem importa
#Product - Ordem importa e repete valores únicos
from itertools import permutations, combinations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'João', 'Maria', 'Emanuel', 'Larissa'
]

camisetas = [['preta', 'branca'],
             ['p', 'm', 'g'],
             ['masculino, feminino', 'unissex'],
             ['algodão', 'poliester'],
]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))