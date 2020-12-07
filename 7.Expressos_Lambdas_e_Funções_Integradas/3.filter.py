"""
filter
filter(): serve para filtrar dados deuma determinada coleção

#biblioteca de dados estatistioos
import statistics

#dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

#calculando a media dos dados com a função mean()
media = statistics.mean(dados)
print('Média:', media)


#como a função map()e filter() recebarao dois paramentros
# sendo um função e outro interavel

res = filter(lambda x: x >= media, dados)
print('Maiores', list(res))

resMenor = filter(lambda x: x < media, dados)
print('Menores', list(resMenor))

paises = ['', 'Argeuntina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)

resPaises = filter(None, paises)
print(list(resPaises))

#diferença entre map() e filter()
#map() recebe dois parametros:
# - função interavel
# - e um interavel
# e retorna um objeto mapeando a funçõ para cadaelemento do iteravel

#filter() Recebe dois parametro
# - uma função
# - e um interavel
# e retorna um objeto filtrado aapenas os elementos de acordo com a função
"""
#Exemplo mais completo
usuarios = [
    {
        'username': 'Samuel',
        'tweets': ['Eu amo bolos', 'Amo pizza']
    },
    {
        'username': 'Carla',
        'tweets': ['Eu amo meu gato']
    },
    {
        'username': 'Jeff',
        'tweets': []
     },
    {
        'username': 'bob123',
        'tweets': []
    },
    {
        'username': 'doggo',
        'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']
    },
    {
        'username': 'gal',
        'tweets': []
    },
]

#filtrar os usuarios inativos
print(usuarios)
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)