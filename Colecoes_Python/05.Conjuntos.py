"""
Conjuntos
"""
print('Forma 1 - conjunto ignora numers repetidos')
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 1})
print(s)
print(type(s))

print('\nForma 2')
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))
if 3 in s:
    print('tem o 3')
else:
    print('nao tem')

print('\nForma 3 - sem ordem')

lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'lista: {lista} elementos {len(lista)}')

tupla = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'tupla: {tupla} elementos {len(tupla)}')

dicionario ={}.fromkeys(lista, 'dict')
print(f'Dicionario: {dicionario} elementos {len(dicionario)}')

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} elementos {len(conjunto)}')