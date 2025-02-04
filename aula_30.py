"""
Constantes no python são usado como uma variavel que nunca vai mudar
ou seja, para representar essa constante, nós vamos usar a variavel com letras maicusulas
diferentemente quando usavamos 'algo = 1', isso é uma variavel
uma constante desse algo, seria 'ALGO = 1', isso indica que é uma constante que não vai mudar
outra coisa que é comum, é que como nós vamos fazer o código para alguem,
muitas condições dentro de um if é ruim de ler, logo, o ideal eh usar o menor numero de
operadores dentro de um if para fazer o mesmo código por exemplo
e no caso, se tiver muitos espaços
        < dessa forma, também fica ruim para ler o código.
"""
velocidade = 61 #velocidade atual do carro
local_carro = 100 #posição do carro

RADAR_1 = 60 #limite de velocidade do radar_1
LOCAL_1 = 100 #posição do radar 1
RADAR_RANGE = 1 #distância de onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1 #variavel para diminuir o If, para não usarmos tantas
#condições em um só if
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade do carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou o radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')

