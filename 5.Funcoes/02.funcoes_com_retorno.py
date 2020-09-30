"""
Funções com retorno
return
1 - ela finaliza a função , ou seja sai da execução  da funçao
2 - podemos ter uma função, diferentes returns
3 - podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores


numeros = [1, 2, 3, 4, 5]
#pop retorna o ultimo numero da lista
ret_pop = numeros.pop()
print(f'retorno de pop:{ret_pop}')
#print nao retorna a nada
ret_pr = print(numeros)
print(f'O retorno de print: {ret_pr}')
"""
"""
funções que retornam valores, devem retornar esses valores com a palavra reservada return

def quadrado_de_7():
    return 7*7
ret = quadrado_de_7()
print(f'forma1\n'
      f'Retorno: {ret}')
print(f'\nforma2\n'
      f'Retorno: {quadrado_de_7()}')

print('Exemplo 1')
def diz_oi():
    print('estou execultando antes do return')
    return 'oi'
    print('estou execultando depois do return')   #essa linha não sera execultada pois esta depois do return

print(diz_oi())
"""
print('Exemplo 2')
def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'
print(nova_funcao())
