"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""
farhren = float(input('Digite a temperatura em graus Fahrenheit'))
Celsius = 5 * ((farhren-32) / 9)
print('O valor em graus Celsius é: {}'.format(Celsius))