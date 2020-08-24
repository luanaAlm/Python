"""Faça um Programa que peça as 4 notas bimestrais e mostre a média."""
media = 0
soma = 0
for m in range(1, 5):
    nota = int(input('Digite a {}° nota: '.format(m)))
    soma = soma + nota
    media = soma / 4
print('A sua média é: {}'.format(media))