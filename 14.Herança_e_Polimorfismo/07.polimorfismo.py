"""
POO - Polimorfismo
Quando um método é reimplementado da classe pai em classes filhas, realiza-se uma sobrescrita de
método (Overriding), que é a representação do polimorfismo
"""

class Animal(object):
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar esse método')

    def comer(self):
        print(f'{self.__nome} está comendo...')

class Cachorro(Animal):
    def __init__(self, nome):
        super(Cachorro, self).__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau')

class Gato(Animal):
    def __init__(self, nome):
        super(Gato, self).__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau')

class Rato(Animal):
    def __init__(self, nome):
        super(Rato, self).__init__(nome)

#testes
felix  = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()