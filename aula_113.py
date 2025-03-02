# groupby = agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'A'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Larissa', 'nota': 'B'},
    {'nome': 'Emanuel', 'nota': 'B'},
    {'nome': 'Lucas', 'nota': 'C'},
    {'nome': 'Felipe', 'nota': 'C'},
    {'nome': 'Junior', 'nota': 'D'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)