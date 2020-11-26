"""
List Comprehension
pode-se gerar novas listas com dados prcessados a partir de outro interável
"""
"""
#sintaxe do List Comprehension
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res)
print([numero * 2 for numero in [1, 2, 3, 4, 5]])
"""
nome = 'Geek University'
print([letra.upper() for letra in nome])

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome
amigos = ['maria', 'julia', 'carlos', 'andrá', 'marcos']
print([caixa_alta(amigo) for amigo in amigos])
