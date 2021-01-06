"""
POO - Herança Múltipla
é a possibilidade de uma classe herdar de múltiplas classes, fazendo com que a classe filha herde todos
os atributos e metodos de todas as classes herdadas

OBS: a herança multipla pode ser feita de duas maneiras:
    -Por multiderivação direta;
    -Por multiderivação indireta;

#EX1 multiderivação direta
class Base1:
    print('1')

class Base2:
    print('2')

class Base3:
    print('3')

#herda as duas classes
class MultiderivadaDir(Base1, Base2, Base3):
    pass

#EX2 multiderivação indireta
class Base1:
    print('1')

class Base2(Base1):
    print('2')

class Base3(Base2):
    print('3')

#herda as duas classes
class MultiderivadaInd(Base3):
    pass

print(MultiderivadaDir)
print(MultiderivadaInd)
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

baleia = Aquatico('Willy')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar()) #Method resolution order - MRO