"""
Loop for
é uma estrutura de repetição
"""
#for 1 interando uma string
nome ='Geek University'
lista =[1, 3, 5, 7, 9]
numeros = range (1,10)


for letra in nome:
    print(letra)

# for 2 iterando sobre uma lista
for numero in lista:
    print(numero)

#for 3 interando sobre o renge
for numero in range(1, 10):
    print(numero)
    
#enumerate numera cada letra pondo assim um indice a cada letra
for indice, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

print("Soma")
qtd = int(input("Quantas vezes o loop deve rodar?"))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'informe o {n}/{qtd} valor: '))
    soma = soma + num
    print(f'A soma e: {soma}')


print("imprimir todas as letras em uma so linha")
for letra in nome:
    print(letra, end='')

for _ in range(3):
    for num in range(1,11):
        print('\U0001F60D' * num)