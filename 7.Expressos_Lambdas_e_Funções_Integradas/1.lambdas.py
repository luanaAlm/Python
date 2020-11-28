"""
São funçõoes sem nome ou seja função anônimas
"""

def funcao(x):
    return 3 * x + 1
print(funcao(7))
print(funcao(4))

#Expressao lambda
print('-- Lambda --')
calc = lambda x: 3 * x + 1
print(calc(7))
print(calc(4))

#lambda com varias entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('maria', 'sousa'))
print(nome_completo('FERNANDA     ', 'soares'))