"""
Liatas Aninhadas
"""
listas = [[1, 2, 3], [5, 5, 6], [7, 8, 9]]
print(listas)
print(type(listas))

#Acessando os dados
#cadas lista é um elemento
print(listas[0])
print(listas[0][1])
print(listas[ 2][1])

#interando com loops em uma lista aninhada
print('-- lista com loop --')
for lista in listas:
    for num in lista:
        print(num)

print('-- List Comprehension --')
#for lista in listas
#(valor) for valor in lista
[[print(valor) for valor in lista] for lista in listas]

print('-- tabuleiro matriz 3x3 --')
#colunas: for valor in range(1, 4)
#linhas: [numero for numero in range(1, 4)]
tabuleiro =[[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

print('-- Jogadas para o jogo da velha --')
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)