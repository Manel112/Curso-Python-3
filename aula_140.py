# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    cpf = '1234'
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome_classe(self):
        print('To na Pessoa')
        print(self.nome, self.sobrenome, self.__class__,__name__)

class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('To no Cliente')
        print(self.nome, self.sobrenome, self.__class__,__name__)

class Aluno(Pessoa):
    # cpf = '2138123'
    ...
c1 = Cliente('Emanuel', 'Lucas')
a1 = Aluno('Larissa', 'Paganini')
# print(c1.nome, c1.sobrenome)
# print(a1.nome, a1.sobrenome)
c1.falar_nome_classe()
a1.falar_nome_classe()
print(a1.cpf)