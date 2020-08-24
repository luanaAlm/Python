"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
"""
calArea = 0
dobro = 0
area = float(input('digite a area do quadrado: '))
calArea = area * area
dobro = calArea * 2
print('O valor da area é: {}'. format(calArea))
print('O dobro desta área é: {}'.format(dobro))