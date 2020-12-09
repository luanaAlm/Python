"""
Sorted() -> serve para ordenar
Sempre retorna uma lista com os elementos ordenandos
"""
"""
numeros = (6, 1, 8, 2)
print('lista original', numeros)
print('lista com sorted', sorted(numeros)) #gera uma nova lista
#a antiga lista fica igual
print('lista apos o sorted', numeros)

#adicionando parametros
print('sorted com o reverse', sorted(numeros, reverse=True))

#Exemplo mais complexo
usuarios = [
    {'username': 'Samuel', 'tweets': ['Eu amo bolos', 'Amo pizza']},
    {'username': 'Carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'Jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': [], 'cor': 'amarelo'},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': []},
]
print(usuarios)
print(sorted(usuarios, key=lambda usuario: usuario['username']))
"""

musicas = [
    {'titulo':'Heathens','tocou': 25},
    {'titulo':'Natural','tocou': 50},
    {'titulo':'What Lovers Do ft. SZA','tocou': 36},
    {'titulo': 'That’s What I Like', 'tocou': 57}
]
print('menos tocada para a mais tocada')
print(sorted(musicas, key=lambda musica: musica['tocou']))

print('mais tocada para a menos tocada')
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
