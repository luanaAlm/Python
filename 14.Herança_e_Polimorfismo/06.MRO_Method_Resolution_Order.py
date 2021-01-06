"""
MRO - Method Resolution Order
Ordem e execuçao do método
Podemos conferir a ordem MRO de 3 formas:
    -via propriedade da classe __mro__
    -via método
    -via help
"""
class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} e sou do mar!'

class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} e sou da terra!'

class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)

    #def cumprimentar(self):
    #    return f'Pinguim'

print('Pinguim')
tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())

"""
Terrestre
Eu sou Tux e sou da terra!
"""

"""
Aquatico
Eu sou Tux e sou do mar!
"""