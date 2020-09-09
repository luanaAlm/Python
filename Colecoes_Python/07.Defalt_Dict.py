"""
é o dicionario de todas as funções
Defalt Dict:Ao criar um dicionario utilizando-o, nos informammos o valor defalt,
podendo utilizar a lambda paara isso. Esse vaalor sera utilizado sempre que não
houver um valor definido. Caso tentamos acessar uma chave que nao existe. Essa
chave sera criada e o valor defall sera atrribuido

dicionario= {'curso': 'Programação em python'}
print(dicionario)
print(dicionario['curso'])
"""
#fazendo import
from collections import defaultdict
dicionario = defaultdict(lambda:0)
dicionario ['curso'] ='Programação em python'
print(dicionario)
print(dicionario['outro'])
print(dicionario)