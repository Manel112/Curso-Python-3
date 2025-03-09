# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, asdict, astuple

@dataclass(init= False)
class Pessoa:
    nome: str
    # idade: int
    sobrenome : str

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_completo = f'{self.nome} {self.sobrenome}'
    
    def __post_init__(self): #o post init é executado depois do init
        #se não tiver um init, o post init não será executado
        print('POST INIT')
    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'
    
    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)

if __name__ == '__main__':
    p1 = Pessoa('Emanuel', 'Lucas')
    p1.nome_completo = 'Emanuel Lucas'
    # p2= Pessoa('Emanuel', 23)
    print(asdict(p1))
    print(astuple(p1))
    print(p1.nome_completo)