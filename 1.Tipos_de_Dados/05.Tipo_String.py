"""
Tipo String
"""
nome = 'Aspas simples'
print(nome)
print(type(nome))

nome = """Luana Almeida"""
print(nome)
print(type(nome))

nome1 = "Gina's bar"
print(nome1)
print(type(nome1))

#pular linha
nome2 = 'luana \nalmeida'
print(nome2)

nome3 = """Cassio
almeida"""
print(nome3)

# nome maiusculo
print(nome.upper())

# nome minusculo
print(nome.lower())

# Lista de strings
print(nome.split())
# letras
print(nome[5:10])
# inverter a ordem da string
print(nome2[::-1])
# trocar letras
print(nome.replace('a', ' '))