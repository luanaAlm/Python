"""
Trabalhando com JSON e Pickle

JSON -> JavaScript Object Notation
API -> São meios de comunicação entre os serviços oferecidos por empresas (ex: facebook, youtube, twitter)
e terceiros (ex: desenvolvedores)
"""

import json
"""
ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220V', 2340 )}])

print(type(ret))
print(ret)

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix  = Gato('Felix', 'Vira-lata')
print(felix.__dict__) #aspas simples

ret = json.dumps(felix.__dict__) #aspas duplas
print(ret)
"""

#interando o json com o Pickle
#Instalar a biblioteca
# pip install jsonpickle

import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca
"""
#gerando o arquivo json/pickle
felix  = Gato('Felix', 'Vira-lata')

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)
"""
#recuperando o arquivo json/pickle
with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)