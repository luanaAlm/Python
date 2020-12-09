"""
Min(): retorna o menor valor em um interavel o ou menor de dois ou mais elementos
Max(): retorna o maior valor em um interavel o ou maior de dois ou mais elementos
"""

"""
lista = [1, 8, 4, 99, 32, 100]
print('lista: ', lista)
print('Max: ', max(lista))
print('Min: ', min(lista))

tupla = (1, 8, 4, 99, 32, 100)
print('tupla: ', tupla)
print('Max: ', max(tupla))
print('Min: ', min(tupla))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 32, 'f': 100}
print('dicionario: ', dicionario)
print('Max: ', max(dicionario))
print('Max: ', max(dicionario.values()))
print('Min: ', min(dicionario))
print('Min: ', min(dicionario.values()))
"""

nomes = ['Isaac Asivon', 'Marcos Vinicios', 'Gorete V. Lacerda', 'Lazaro Sousa', 'Maria O. C. Vilani',
           'Julioc Cesar', 'H. G. Cruz', 'Reinaldo Maraes', 'Daniel Marques', 'Heitor Enzo']
#considera a o ordem alfabetica
print(max(nomes))
print(min(nomes))
#maior nome
print('maior nome: ',max(nomes, key=lambda nome: len(nome)))
#menor nome
print('menor nome: ',min(nomes, key=lambda nome:  len(nome)))




musicas = [
    {'titulo':'Heathens','tocou': 25},
    {'titulo':'Natural','tocou': 50},
    {'titulo':'What Lovers Do ft. SZA','tocou': 36},
    {'titulo': 'That’s What I Like', 'tocou': 57}
]
print('Mais tocada: ',max(musicas, key=lambda musica: musica['tocou']))
print('Menos tocada:',min(musicas, key=lambda musica: musica['tocou']))

print('Titulo maio tocado: ',max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print('Titulo menos tocado: ',min(musicas, key=lambda musica: musica['tocou'])['titulo'])

