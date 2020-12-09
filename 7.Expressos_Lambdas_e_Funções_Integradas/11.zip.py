"""
zip(): cria um interael (zip object) que agrega elemento de cada um dos iteraveis passados como entrada
em pares
"""
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
zip1 = zip(lista1, lista2, 'abc')

print('list: ', list(zip1))
print('type: ', type(zip1))
print('tuple: ', tuple(zip1))
print('set: ', set(zip1))
print('dict: ', dict(zip1))
