#Atributos de classe

class Pessoa:
    ano_atual = 2025 #isso é chamado de atributo de classe, ou seja, essa variável 
    #vai ser ela, sempre que chamarmos essa classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_de_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Emanuel', 23)
p2 = Pessoa('Larissa', 21)

print(Pessoa.ano_atual)

print(p1.get_ano_de_nascimento())
print(p2.get_ano_de_nascimento())