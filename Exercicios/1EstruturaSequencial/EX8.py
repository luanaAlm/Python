"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
soma = 0
valor = float(input('Quanto você ganha por hora? '))
hora = int(input('Número de horas trabalhadas no mês? '))
soma = valor * hora
print('Seu ganho é: {}'.format(soma))
