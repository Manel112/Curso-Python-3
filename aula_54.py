"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista_de_compras = []
while True:
    print('Selecione uma opção:')
    opcao = input('[i]nserir, [a]pagar, [l]istar: ')
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista_de_compras.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar')
        try:
            indice = int(indice_str)
            del lista_de_compras[indice]
        except ValueError:
            print('Por favor, digite um numero inteiro')
        except IndexError:
            print('Por favor, digite um número da lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')
        if len(lista_de_compras) == 0:
            print('Nada pra listar')
        for i, valor in enumerate(lista_de_compras):
            print(i,valor)
    else:
        print('Por favor, escolha i, a, ou l')


    