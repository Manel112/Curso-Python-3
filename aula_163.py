# Valores padrão e field em dataclasses
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import asdict, astuple, dataclass
from dataclasses import dataclass, field


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    nome: str = field(
        default='MISSING', repr=False
    )
    sobrenome: str = 'Not sent'
    idade: int = 100 #apenas valores IMUTAVEIS
    enderecos: list[str] = field(default_factory=list) #faz com que a list, crie uma nova lista
    #se for usar algo mutavel, usar a função field


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    # print(asdict(p1).keys())
    # print(asdict(p1).values())
    # print(asdict(p1).items())
    # print(astuple(p1)[0])
    p1 = Pessoa()
    # print(fields(p1))
    print(p1)