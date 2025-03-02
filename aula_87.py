#Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print( b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

#args e kwargs
#args (ja vimos)
#kwargs - keyword arguments (argumentos nomeados)


pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 23,
    'altura': 1.78
}

pessoa_completa = {**pessoa, **dados_pessoa}  #** os dois asteriscos pega os valores do dicionario e desempacota no dicionario que queremos.
# print(pessoa_completa)

def mostro_argumentos_nomeados(*args, **kwargs): #kwargs, são argumentos nomeados
    print('NÃO NOMEADOS:', *args)

    for chave,valor in kwargs.items():
        print(chave,valor)

# mostro_argumentos_nomeados(1,2, nome='Joana', qlq=123,)
mostro_argumentos_nomeados(**pessoa_completa)