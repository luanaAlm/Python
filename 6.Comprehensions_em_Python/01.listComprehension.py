"""
List Comprehension
pode-se gerar novas listas com dados prcessados a partir de outro interável
"""

#sintaxe do List Comprehension
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res)