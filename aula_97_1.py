#try, except, else e finally
#o try e except são feitos para tratar erro, ou seja, caso aconteça algum erro
#na execução do programa, podemos usar para trata-lo
#por exemplo:

# a = 20
# b = 0 #numa divisão por zero, vai dar o erro ZeroDivisionError (usa PascalCase)
# print(b[0])
# c = a / b #podemos tratar com o try/except


try:
   a = 20
   b = 0
#    print(b[0])
   c = a / b #pulou daqui, pro except
except ZeroDivisionError as e: #podemos tratar qualquer erro
    print(e) #podemos usar o as, para definirmos o erro a uma variavel e quando imprimimos o erro
    #aparece para o usuário o devido erro, sem termos q usar uma string pra representar ele
except TypeError:
    print('TypeError')
except (IndexError, NameError):
    print('Index Error + NameError')
except Exception: #esse é o maior erro de todos, que trata qualquer erro.
    #caso não sabemos o que está acontecendo, o exception tratará de todos, por exemplo
    #se tivermos um index error, o exception trata dele.
    print('Erro desconhecido')

#tambem podemos tratar 2 erros de uma vez só, usando como uma tupla
print('Continuar...')