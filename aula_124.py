#Métodos em instâncias de classe Python
#Hard coded - é algo que foi escrito diretamento no código, ex: carro = 'Fusca'
#Classe - é o molde (geralmente sem dados)
#Instância da classe (objeto) - tem os Dados
#Uma classe pode gerar várias instâncias
#Na classe o self é a própria instância

class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')

string = 'Emanuel'
print(string.upper())


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()