import importlib
import aula_101_m

for i in range(10):
    importlib.reload(aula_101_m)
    print(i)

print('Fim')

#o python importa as coisas como singlethon, ou seja, ele importa uma vez
#e caso peça de novo, ele ja ta na memoria, então não importa mais vezes
#com a importlib, nós podemos dar reload naquilo que a gente quer, ou seja,
#recarregamos aquilo que pedimos, com isso, aparecendo mais vezes ao invés de uma só
#porém, é incomum usarmos isso