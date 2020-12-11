"""
Try/Except
serve para tratar erros que ocorrem no código
try:
    execução problematica
Except:
    o que deve ser feito no caso do problema

try:
    geek()
except:
    print('Deu algum problema')

#erro específico
try:
    geek()
except NameError:
    print('Erro: fução inesistente')

try:
    len(5)
except TypeError as err:
    print(f'Erro: {err}')

#diversoso tratamentos de uma vez
try:
    len(5)
except NameError as erra:
    print(f'Erro: {erra}')
except TypeError as errb:
    print(f'Erro: {errb}')
"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'nome': 'geek'}
print(pega_valor(dic, 'game'))
print(pega_valor(1, 'game'))