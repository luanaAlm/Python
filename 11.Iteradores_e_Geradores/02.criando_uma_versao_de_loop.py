"""
Criando sua própria versão de loop
"""
for num in [1, 2, 3, 4, 5]:
    print(num)
print('\n')
for letra in 'Geek University':
    print(letra)

def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
print('\n')
meu_for('Geek University')
numeros = [1, 2, 3, 4, 5]

meu_for(numeros)