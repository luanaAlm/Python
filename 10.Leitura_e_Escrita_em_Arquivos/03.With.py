"""
With: é utilizado para criar um contexto de trabalho onde os recursos utilizadas são fechados
após o bloco with
"""
#forma profissional de manipular arquivos
with open('teste.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)