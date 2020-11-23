"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
num = int(input('Digite o numero'))
print(f'O número {num}')
if num < 0:
    print('Negativo')
else:
    print('Positivo')