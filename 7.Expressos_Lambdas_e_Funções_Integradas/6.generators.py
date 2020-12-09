"""
Generators
"""
"""
nomes = ['Carlos', 'Cassio', 'Camila', 'Daniel', 'Cristina', 'Vanessa', 'Hugo']
print(any(nome[0] == 'C' for nome in nomes))

res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)
"""
#getsizeof retorna a quantidade de bytesem memória do elemento passado como parametro
from sys import getsizeof
#quanto de memoria a string geek oculpa de memória em bytes
"""
print('1)',getsizeof('Geek'))
print('2)',getsizeof('As funções do gerador permitem que você declare uma função que se comporta '
                'como um iterador, ou seja, pode ser usada em um loop for.'))
print('3)',getsizeof(9))
print('4)',getsizeof(91))
print('5)',getsizeof(6543216546546))
print('6)',getsizeof(True))
"""
#gerando uma lista de números List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

#gerando uma lista de números Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

#gerando uma lista de números Dictionary Comprehension
dic_comp = getsizeof({x:x * 10 for x in range(1000)})

#gerando uma lista de números com Generators
gen = getsizeof(x * 10 for x in range(1000))

print('List Comprehension', list_comp, 'bytes')
print('Set Comprehension', set_comp, 'bytes')
print('Dictionary Comprehension', dic_comp, 'bytes')
print('Generators', gen, 'bytes')



