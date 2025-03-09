# Classes abstratas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição
# de novas classes. Elas podem forçar outras classes
# a criarem métodos concretos. Também podem ter
# métodos concretos por elas mesmas.
# @abstractmethods são métodos que não têm corpo.
# As regras para classes abstratas com métodos
# abstratos é que elas NÃO PODEM ser instânciadas
# diretamente.
# Métodos abstratos DEVEM ser implementados
# nas subclasses (@abstractmethod).
# Uma classe abstrata em Python tem sua metaclasse
# sendo ABCMeta.
# É possível criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorator mais interno.

#como não queremos que a classe Log seja usada, nós transformamos ela em uma classe
#abstrata, isso significa que, ela não poderá ser usada em lugar nenhum, somente as classes
#filhas dela, poderão ser usadas.
#para usar a classe abstrata, preciasmos importar ela
from abc import ABC, abstractmethod

class Log(ABC):  
    #para colocarmos o abstracmethod, colocamos o Log como herdeiro de ABC
    @abstractmethod
    def _log(self, msg):... #não precisamos mais do corpo de _log e usamos somente 
    #o decorador, @abstractmethod
    #agora, nossa classe Log, é abstrata e não poderá ser usada no código
        
    def log_error(self,msg):
        return self._log(f'Error: {msg}')
    
    def log_sucess(self,msg):
        return self._log(f'Sucess: {msg}')
    
class LogPrintMixin(Log):
    def _log(self,msg):
        print(f'{msg} ({self.__class__.__name__})')

l = LogPrintMixin()
l.log_error('Oi')