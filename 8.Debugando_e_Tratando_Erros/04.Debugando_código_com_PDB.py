"""
Debugando código com PDB (Python debugger)
"""
def dividir(a, b):
    try:
        return int(a)/ int(b)
    except(ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))

import pdb
nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em python'
final = nome_completo + ' faz o curso ' + curso
print(final)
