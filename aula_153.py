# Context Manager com função - Criando e Usando gerenciadores de contexto
# Uma outra forma de abrir um arquivo com context manager é usando o decorador
# e fazendo dele um generator e podemos tratar as excessões com try, finally

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()


with my_open('aula153.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)