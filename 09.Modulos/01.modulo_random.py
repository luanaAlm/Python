"""
Módulos são outros arquivos python
São úteis para reutilização de códigos
Módulo Random -> Possui várias funçoes para geração de números  pseudo-aleatório
"""

"""
#forma 1 - importando todo o modulo
#ficará na memória
import random
#primeiro random -> pacote
# segundo random() -> função
print(random.random())

#Forma 2 - Importando uma função especifica do random
from random import random

for i in range(10):
    print(random())
print('\n')
#uniform() -> Gera um número pseudo-aleatório entre os valores estabelecidos
from random import uniform
for i in range(10):
    print(uniform(3, 7)) #O 7 não será incluido
print('\n')
#randint() -> Gera um número pseudo-aleatório entre os valores estabelecidos
from random import randint
for i in range(6):
    print(randint(1, 61), end='. ')
print('\n')
#choice() -> Mostra um valor aleatório entre interáveis
from random import choice
jogador = ['pedra', 'papel', 'tesoura']
print(choice(jogador))    
"""
print('\n')
#shuffle() -> Embaralha números interáveis
from random import shuffle
cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)
shuffle(cartas)
print(cartas)
print('Carta:',cartas[0])