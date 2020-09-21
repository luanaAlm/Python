"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário
de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""
peso = float(input('Digite o peso (Kg) do peixe: '))
preco = int(input('Digite o preço(Kg) do peixe: \n'))

excesso = (50 - peso)
multa = excesso * 4
valor = preco + multa

if peso <= 50:
    print('Peixe sem multa por excesso de peso')
    print('Preço a pagar: {}'.format(preco))
else:
    print('Valor do excesso: {}'.format(excesso))
    print('Valor a pagar: {}'.format(valor))

