from sys import path

import aula_102_package.modulo
# from aula_102_package import modulo
# from aula_102_package.modulo import *
from aula_102_package import soma_do_modulo, nova_variavel, variavel

# from aula99_package.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula_102_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)