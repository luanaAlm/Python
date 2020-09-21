"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta
é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
arredonde os valores para cima, isto é, considere latas cheias.
"""
area = float(input('Area a ser pintada : '))
lata = 108
#valLata = 80
galao = 64.8
#valGalao = 25
print('Formas de compra'
      '\nApenas latas de 18 litros: Digite 1'
      '\nApenas galões de 3,6 litros: Digite 2'
      '\nMisturar latas e galões: Digite 3')
num = int(input())
if num == 1:
    valorLata = float(lata * 80)
    print('Latas para pintar: {}'.format(area/lata))
    print('O valor a pagar: {}'.format(valorLata))
elif num == 2:
    valorGalao = float(galao * 25)
    print('Latas para pintar: {}'.format(area /(galao)))
    print('O valor a pagar: {}'.format(valorGalao))
elif num == 3:
    valorGalao = float(galao * 25)
    valorLata = float(lata * 80)
    soma = valorLata + valorGalao
    print('Latas para pintar: {}'.format(area / (galao+lata)))
    print('O valor a pagar: {}'.format(soma))
else:
    print('Operação invalida')