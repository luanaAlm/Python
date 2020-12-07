"""
reduce
a partir da versao 3+ nao é mais uma função integrada (built-in)
agors deve-se importar e utilizar essa função a partir do modulo 'functools'

reduce(funcao, dados)
A função reduce() funciona da seguinte forma:
    Passo 1: resl = f(a1, a2) #aplica a função nos dois primenros elementos da coleção e guarda o resultado
    Passo 2: res2 = f(res1, a3) #aplica a função passando o resultado do passo1 msis o terceiro elemento
    e guarda o resultado

    Isso é repetido ate o final
    Passo3: res3 = f(res2, a4)
    .
    .
    .
    PassoN: resN = f(resM, aN)
"""
#Multiplicar os numeros de uma lista
from functools import reduce
dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]
mult = lambda x, y: x * y
res = reduce(mult, dados)
print(res)

#loop normal
res = 1
for n in dados:
    res = res * n
print(res)