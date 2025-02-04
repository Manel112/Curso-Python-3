# Exercicio Guiado, Calculadora com while



while True:
    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador desejado: ')
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None
    if numeros_validos is None:
        print("Um ou ambos os números são invalidos.")
        continue
    operadores_permitidos = '-+*/'

    if operador not in operadores_permitidos:
        print('O operador digitado é invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    if operador == '+':
        resultado = num_1_float + num_2_float
        print(resultado)
    elif operador == '-':
        resultado = num_1_float - num_2_float
        print(resultado)
    elif operador == '/':
        resultado = num_1_float / num_2_float
        print(resultado)
    elif operador == '*':
        resultado = num_1_float * num_2_float
        print(resultado)

    sair = input('Para finalizar, digite [s]air, para continuar, digite qualquer coisa: ').lower().startswith('s')

  # sair = sair.lower()  #faz com que o que o usuario digitou, saia minúsculo
  # sair = sair.startswith('s')  #checa se começa com a letra s
    
    if sair is True:
        break
    else:
        continue