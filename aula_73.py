# Funções de Primeira Classe
# High Order Function

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa (funcao, *args):#empacota o resto das variaveis que eu colocar e nao usar
    return funcao(*args) #desempacota as variaveis

print(executa(saudacao, 'Bom dia', 'Emanuel'))  
print(executa(saudacao, 'Bom dia', 'Alana'))  #mesma função, porem mudei os argumentos