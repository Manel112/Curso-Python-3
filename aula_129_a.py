import json
# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
CAMINHO_ARQUIVO = 'aula_129_a.json'

class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_de_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('Emanuel', 23)
p2 = Pessoa('Larissa', 21)
p3 = Pessoa('Felipe', 23)
pessoas = [vars(p1), vars(p2), vars(p3) ]

def fazer_dump():
    with open (CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        print('FAZENDO O DUMP...')
        json.dump(pessoas, arquivo, ensure_ascii=False, indent= 2)

if __name__ == '__main__':
    print('Ele é o __main__')
    fazer_dump()