"""
Try, Except, Else e Finally
Tratamento de código: quando houver entrada de dados pelo usuário
"""

num = 0
try:
    num = int(input('Você digitou um número'))
except ValueError:
    print('Valor incorreto!')
else:
    print(f'Você digitou {num}')
finally:
    print('Tenha um bom dia')