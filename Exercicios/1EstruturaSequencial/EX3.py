"""Faça um Programa que peça dois números e imprima a soma"""
soma = 0
for c in range(1, 3):
    num = (int(input('Digite o {}° um valor: '.format(c))))
    soma = soma + num
print('A soma e: {}'.format(soma))