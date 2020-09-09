"""
Namad Tuple (tuplas nomeadas): sao tuplas diferenciadas onde, especificamos um nome para a mesma e tambem parametyros
tupla=(1,2,3)
print(tupla[1])
"""
from collections import namedtuple
#forma de declaração 1
cachorro = namedtuple('cachorro', 'idade raca nome')
#forma de declaração 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')
#forma de declaração 3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

#Acessando os Dados
#forma 1
ray = cachorro(idade=8, raca='viralata', nome='Sansão')
print(ray)
print('-----')
#forma 2
print(ray[0])
print(ray[1])
print(ray[2])
#forma 3
print('-----')
print(ray.idade)
print(ray.raca)
print(ray.nome)
