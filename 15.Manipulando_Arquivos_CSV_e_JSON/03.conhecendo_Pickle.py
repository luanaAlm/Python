"""
Conhecendo o Pickle
Realiza o seguinte processo:
Objeto python -> Binarizaçõo (serialização)
Binarizaçõo -> Objeto python (deserialização)
OBS: Pickle não é seguro contra dados maliciosos e dessa forma não é recomendado trabalhar com arquivos
Pickle de pessoas desconecidas
"""
import pickle

class Animal:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.nome} está comendo')

class Gato(Animal):
    def __init__(self, nome):
        super(Gato, self).__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando')

class Cachorro(Animal):
    def __init__(self, nome):
        super(Cachorro, self).__init__(nome)

    def late(self):
        print(f'{super.nome} está latindo')
"""
felix = Gato('Felix')
pluto = Cachorro('Pluto')

#Fazendo escrita em arquivos pickle
with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)
"""

#Fazendo leitura em arquivos pickle
with open('animais.pickle', 'rb') as arquivo: #rb leitura
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(gato)}')