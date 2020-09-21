"""
Ordered Dict: é um dicionario que garante a ordem de inserção dos dados
"""
from collections import OrderedDict
print('exemplo 1')
dicionario = OrderedDict({'a':1, 'b':2, 'c':3, 'd':4, 'e':5})
for chave, valor in dicionario.items():
    print(f'chave={chave} e valor={valor}')

print('\nexemplo 2')
odic1 = OrderedDict({'a':1, 'b':2})
odic2 = OrderedDict({'a':2, 'b':1})
print(odic1 == odic2)


