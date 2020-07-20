"""
Saindo do loop com break
"""
print('Exemplo 1, com for')
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('sair do numero!')

print('-----')
print('Exemplo 2, com while')
while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break
