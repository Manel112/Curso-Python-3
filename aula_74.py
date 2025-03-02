"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao): #diferente do anterior, agora nos adiamos a função saudar
    def saudar(nome): #"automatizamos", para que nós possamos colocar apenas diferentes nomes
        return f'{saudacao}, {nome}!' #retornamos as duas funções
    return saudar #retornamos saudar, mas sem fechar a função

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Emanuel', 'Lucas', 'Larissa', 'Joao']:
    print(falar_boa_noite(nome)) #aqui fechamos a função saudar com os () e isso é o closure
    print(falar_bom_dia(nome))
