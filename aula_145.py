# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.

from abc import ABC, abstractmethod

class AsbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    # @property
    # @abstractmethod
    # def name(self):
    #     ...
    @property
    def name(self):
        return self._name
    
    @name.setter
    @abstractmethod
    def name(self,name): ...



class Foo(AsbstractFoo):

    @AsbstractFoo.name.setter
    def name(self, name):
        self._name = name #essa é a segunda forma de fazer, usamos o nome da classe no setter
    # @property
    # def name(self):
    #     return self._name

#essa é uma das formas, uma outra formas de fazer
#uma outra forma é se o setter receber a abstract method
    # @name.setter
    # def name(self, name): 
    #     self._name = name

    # def __init__(self, name):
    #     super().__init__(name)
    #     # print('Sou inútil')

foo = Foo('Bar')
print(foo.name)