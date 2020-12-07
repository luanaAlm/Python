"""
all() retorna a True se todos os elementos do interavel sao verdadeiros ou ainda se interavel
esta vazio
any() Retorna a true se qualquer elemento do interavel for verdadeiro, se o interavel tiver vazio , retorna false
"""
#Exemplo all()
print(all([0, 1, 2, 3, 4])) #sera falso por cont do 0

print(all([1, 2, 3, 4])) #sera verdadeiro pois nao tem o 0

print(all([]))

print(all(['geek']))

nomes = ['Carlos', 'Cassio', 'Camila', 'Daniel']
print(all(nomes[0]=='C' for nome in nomes))

#Exemplo any()
print(any([0, 1, 2, 3, 4, 5]))
print(any([0, False, {}, (), []]))