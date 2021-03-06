"""
tuple

É parecido com listas porem sao representadas por parenteses, elas sao imutaveis.
Sua operação gera uma nova tupla
"""

print('tuple 1')
tupla1 = (1,2,3,4,5,6)
print(type(tupla1))
print(tupla1)

print('------')
print('tuple 2')
tupla2 = 1,2,3,4,5,6
print(type(tupla2))
print(tupla2)

print('------')
print('tuple 3 - ISSO NAO E UMA TUPLE')
tupla3 = (4)
print(type(tupla3))
print(tupla3)

print('------')
print('tuple 4')
tupla4 = 4,
print(type(tupla4))
print(tupla4)

print('------')
print('tuple 5 - com ranger')
tupla5 = tuple(range(11))
print(type(tupla5))
print(tupla5)

print('------')
print('tuple 6 - não é adicionado valores ')
tupla6 = ("Feliz Aniversário", "Programação Python")
escola, curso = tupla6
print(escola)
print(curso)

print('------')
print('tuple 7 - somente se os valores forem numericos')
print('soma ',sum(tupla1))
print('maximo ',max(tupla1))
print('minimo ',min(tupla1))
print('tamanho ',len(tupla1))

print('------')
print('tuple 8 - Concatenação de tuplas')
tupla7 = (1,2,3)
tupla8 = (4,5,6)
tupla8 = tupla7 + tupla8
print(tupla8)

print('------')
print('Verifica elemento dentro de uma tulpa')
print(3 in tupla1)

print('------')
print('Interando sobre uma tupla')
for n in tupla1:
    print(n)
print('--')
for indice, valor in enumerate(tupla1):
    print(indice,valor)

tupla9 = ('a','b','c','d','a','e')
print(tupla9.count('a'))
escola1 = tuple('Feliz Aniversário')
print(escola1)
print(escola1.count('i'))