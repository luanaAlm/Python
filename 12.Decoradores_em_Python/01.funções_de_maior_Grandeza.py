"""
Higher Order Function - HOF
funções que retornal outras funções como resultado ou mesmo que podemos passar funções como argumentos
para outras funções, e até mesmo criar vaariáveis do tipo funçõesnos programas.
"""
"""
#Ex1
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

print(calcular(12, 2, somar))
print(calcular(12, 2, subtrair))
print(calcular(12, 2, multiplicar))
print(calcular(12, 2, dividir))

#Nested Functions - Funções Aninhadas
# Funções dentro de funções
#EX2

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa #Execultando a função humor()

print(cumprimento('Luana'))
print(cumprimento('Andréia'))


#Retornando funções com outras funções
from random import choice
def faz_me_rir():
    def rir():
        return choice(('hahahahahahaha ', 'kkkkkkkkkkkkk', 'hehehehehehehe'))
    return rir #retornando a função

rindo = faz_me_rir()
print(rindo())
"""
#Ex3
from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahahahaha ', 'kkkkkkkkkkkkk', 'hehehehehehehe'))
        return f'{risada} {pessoa}'
    return dando_risada

rindo2 = faz_me_rir_novamente('Fernanda')
print(rindo2())
print(rindo2())
print(rindo2())