"""
Entendendo Iterators e Iteráveis
Iterator:
    É um objeto que pode ser interado
    Um objeto que retorna um dado, sendo um elemento por vez quando a função next() é chamada

Interable:
    Um objeto que retornará um interator quando a função iter() for chamada
"""

#Interable
nome = 'Magazine'

numeros =[1, 2, 3, 4, 5, 6]

#print(next(nome)) #TypeError: 'str' object is not an iterator
#print(next(numeros)) #TypeError: 'list' object is not an iterator

it1 = iter(nome)
it2 = iter(numeros)
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print('\n')
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print('\n')
for letra in nome:
    print(f' {letra}')