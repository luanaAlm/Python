"""
Built-In -> Módulos integrados já intalados no puthon
"""
#alias (apelidos) para módulos ou funções
import random as rmd
print(rmd.random())


#Import de todas as funções de um módulo usando *
from random import *
print(random())

#Importando todo o modulo
import random
print(random.random())

from random import randint as rdi
print(rdi(5, 56))

#Multiplos immports
from random import (
    random,
    randint,
    shuffle,
    choice
)
print('random:', random())
print('randint:', randint(3, 8))
lista = ['Geek', 'Uniersity', 'Python']
shuffle(lista)
print('shuffle:', lista)
print('choice:', choice('Uniersity'))