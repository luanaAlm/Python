"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
letra = input('Digite f: feminino e m: masculino\n')
if letra == 'm':
    print('Masculino')
if letra == 'f':
    print('Feminino')
else:
    print('Letra invalida')

