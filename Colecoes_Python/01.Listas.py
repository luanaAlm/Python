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