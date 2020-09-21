"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""
n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite um numero inteiro: '))
n3 = float(input('Digite um numero real: '))
produto = (n1 * n1) + (n2 / n2)
soma = (n1 * 3) + n3
elevado = n3**3
print('O produto do dobro do primeiro com metade do segundo é: {}'.format(produto))
print('\nA soma do triplo do primeiro com o terceiro é: {}'.format(soma))
print('\nO terceiro elevado ao cubo é: {}'.format(elevado))