"""
Reversed()
funciona em qqualquer interável
ela inverte o interável
"""
lista = [1, 2, 3, 4, 5, 6]
res = reversed(lista)
print(res)
print(type(res))
#lista
print('Lista: ',list(reversed(lista)))

#tuple
print('Tupla: ',tuple(reversed(lista)))

#Conjunto (set)
print('Conjunto (set): ',list(reversed(lista)))

print('-- forma 1 --')
for letra in reversed('Trabalho de geografia'):
    print(letra, end='')

print('\n-- forma 2 --')
print(''.join(list(reversed('Trabalho de geografia'))))

#loop for reverso
for n in reversed(range(0, 10)):
    print(n)
