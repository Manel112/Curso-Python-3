import re #biblioteca do python para substituir uma coisa em outra tambem
import sys

entrada = input('Digite o seu cpf: ')
cpf = re.sub( #re.sub serve para fazer a substituição
    r'[^0-9]', #o acento circunflexo serve para definir que só pode existir numero de 0 a 9, todo o resto é cortado
    '', #separa com vírgulas e coloca pelo o que vai substituir, no caso, espaço vazio
    entrada #posso digitar qlqr coisa que não seja numero que vai retirar e só vai aparecer
                     #os numeros
)
    # .replace('.', '') \
    # .replace(' ', '') \
    # .replace('-', '') #troca o prieiro argumento com o segundo, no caso, troca o - em nada

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0

for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11

dez_digitos = cpf[:10]
resultado_digito_2 = 0
contador_regressivo_2 = 11


for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -=1
digito_2 = (resultado_digito_2 * 10) % 11

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
if cpf == cpf_gerado:
    print(f'{cpf_gerado} é valido')
else:
    print('CPF Inválido')
