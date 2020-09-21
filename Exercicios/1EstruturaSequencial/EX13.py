"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
altura = float(input('Digite sua altura: '))
print('Qual o seu Sexo?'
      '\nMasculino: Digite 1'
      '\nFeminino: Digite 2')
sexo = int(input())

if sexo == 1:
    homem = (72.7 * altura) - 58
    print('Seu peso idela é: {}'.format(homem))
elif sexo ==2:
    mulher = (62.1*altura) - 44.7
    print('Seu peso ideal é: {}'.format(mulher))
else:
    print('Opção invalida')