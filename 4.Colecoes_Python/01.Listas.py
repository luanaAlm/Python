"""
Listas funcionam como vetores/matriz e pode-se colocar qualquer tipo de dados e dinamicos
"""
type([])
num = 10

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['l', 'u', 'a', 'n', 'a']

lista3 = []

lista4 = list(range(11))

lista4 = list(range(11))

"""
print('Encontrar um numero dentro de uma lista')
if num in lista4:
    print(f'tem o numero {num}')
else:
    print(f'não encontrei o {num}')

print('------')
print('Ordenação de lista')
lista1.sort()
print(lista1)

print('------')
print('Contar as ocorrencias')
print(lista1.count(1))
print(lista2.count('a'))

print('------')
print('Adicionar elementos na lista')
print(lista1)
lista1.append(42) #append() so adiciona uma argumento
print('Adicionar ',lista1)
lista1.append([8,5,6,3]) #append([]) adiciona uma lista dentro de uma outra lista
print('lista dentro de outra')

print('------')
print('condição')
if[8,5,6,3]  in lista1:
    print(lista1)
    print('encontrei os valores na lista')
else:
    print('Não encontrei os valores na lista')

print('------')
print('Adicionar elementos na lista como elemento unico')
lista1.extend([123, 44, 67])
print(lista1)
"""
"""
print('------')
print('inserir elemento de acordo com o indice')
lista1.insert(2, 100)
print(lista1)

print('------')
print('somando duas listas')
lista6 = lista1 + lista2
print('Com soma',lista6)
lista1.extend(lista2)
print('Com extend',lista1)

print('------')
print('Reverter a lista')
lista2.reverse()
print('com reverse',lista2)
print('com [::-1]',lista1[::-1])
"""
"""
print('Copiar uma lista')
lista7 = lista2.copy()
print(lista7)

print('------')
print('tamanho da lista')
print(len(lista2))

print('------')
print('Remover algo da lista')
print(lista2)
lista2.pop()
print(lista2)

print('------')
print('Zerar a lista')
print(lista2.clear())

print('------')
print('separar palavras por espaço')
curso = 'programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

print('------')
print('converter lista em string')
texto = ['programação', 'em', 'Python:', 'Essencial']
print(texto)

print('join, pegar string e tranforma em texto string')
curso = ' '.join(texto)
print(curso)
"""
"""
print('Interando sobre listas')
for elemento in lista2:
    print(elemento)

print('-----')
print('Utilizando While')

carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione mais um ou digite sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)
"""
"""
print('listas com variaveis')
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)
"""
"""
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])
print(cores[-2])
print(cores[-3])
print(cores[-4])

for indice, cor in enumerate(cores):
    print(indice,cor)
"""
"""
print('lista com slice (indice)')

lista = [1, 2, 3, 4]
print(lista[1:])
print(lista[1:])
print(lista[1:3])

print('-----')
print('soma',sum(lista))
print('maximo',max(lista))
print('minimo',min(lista))
print('tamanho',len(lista))
"""

print('copiando lista para outra (shallow copy e Deep copy')
print('forma 1 - DEEP COPY')
lis = [1, 2, 3]
print(lis)
nova = lis.copy()
print(nova)
nova.append(4)
print(lis)
print(nova)
print('-----')
print('forma 1 - SHALLOW COPY')

lis = [1, 2, 3]
print(lis)
nova = lis
nova.append(4)
print(lis)#lista com a adição
print(nova)#vira uma nova lista com a adição
