"""
 Dictionary Comprehension
 sintaxe
 {chave: valor for valor in interavel}
"""
numeros = {'a': 1, 'b': 2,  'c': 3, 'd': 4, 'e': 5}
#cria-se um  novo dicionario
quadrado = {chave:valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

#criando um dicionario a partir de um lista
numeros = [1, 2, 3, 4, 5]
quadrados = {valor: valor ** 2 for valor in numeros}
print(quadrados)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(0,  len(chaves))}
print(mistura)
