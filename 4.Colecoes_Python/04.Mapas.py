"""
Mapas tambem conhecidos como dicionario
são representados por chaves
"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

print('\ninteração sobre o dicionario')

for chave in receita:
    print(f'{chave} : {receita[chave]}')
print('\noutras formas - receitas')
print(receita.keys())
for chave in receita.keys():
    print(receita[chave])

print('\noutras formas - vslores')
print(receita.values())

for valor in receita.values():
    print(valor)

print('\nDesenpacotamento de dicionários')
for chave, valor in receita.items():
    print(f'chave de {chave} : {valor}')

print('soma', sum(receita.values()))
print('maximo', max(receita.values()))
print('minimo', min(receita.values()))
print('tamanho', len(receita.values()))