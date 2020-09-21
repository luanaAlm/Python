""""
counter (Contador)
Ele recebe um interavel como parametro e cria um objeto do tipo collections Counter
que é parecido com um dicionário, contendo como chave o elemento da lista passada como paramentro
e como valor a qquantidade de ocorrencia desse elemento.

"""
#Utilizando o Counter
from collections import Counter
"""
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]
res = Counter(lista)
print(type(res))
print(res)

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
"""
texto = """ O octoeco ou octoecos, também conhecido como os oito tons ou oito modos, 
é o nome dada aos sistemas de oito modos musicais utilizados para a composição de canto 
litúrgico cristão de diversas tradições desde a Idade Média.
Apesar de discordâncias liturgiológicas quanto ao surgimento e difusão do octoeco, 
há consenso quanto à sua origem última na comunidade cristã de Jerusalém, com um sistema 
de oito modos de origem no modalismo clássico (com possível contribuição da tradição hebreia) 
sendo adequado a um ciclo semanal óctuplo, provavelmente no século V. O sistema logo se difundiu 
no Levante e no Cáucaso, onde se desenvolveram tradições autônomas, nomeadamente as do rito sírio 
ocidental (fundamentadas na Casa dos Tesouros), a do armênio e os cantos polifônicos do antigo rito 
da Igreja Ortodoxa Georgiana, hoje substituído 
pelo bizantino. """

palavras = texto.split()
print(palavras)
cont = Counter(palavras)
print(cont)
print(cont.most_common(1))
