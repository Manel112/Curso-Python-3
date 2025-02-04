import random

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))


    contador_regressivo_1 = 10

    resultado_digito_1 = 0

    for digito_1 in nove_digitos:
        resultado_digito_1 += int(digito_1) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11

    dez_digitos = nove_digitos + str(digito_1)
    resultado_digito_2 = 0
    contador_regressivo_2 = 11


    for digito_2 in dez_digitos:
        resultado_digito_2 += int(digito_2) * contador_regressivo_2
        contador_regressivo_2 -=1
    digito_2 = (resultado_digito_2 * 10) % 11

    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
    print(cpf_gerado)