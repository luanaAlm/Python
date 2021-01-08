"""
Escrevendo em arquivos CSV
write() -> escrever
writerow() -> Escreve ma linha
"""

#writer() -> gera um objeto para que possamos esccrever em umm arquivo CSV utilizando o método
#writerow() -> para escrever cada linha, este método recebe uma linha
"""
from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None #variavel
    escritor_csv.writerow(['Título', 'Gênero', 'Duração']) #cabeçalho
    while filme != 'sair':
        filme = input('Informe o nome do filme')
        if filme != 'sair':
            genero = input('Informe o gênero')
            duracao = input('Informe a duração em min')
            escritor_csv.writerow([filme, genero, duracao])
"""

#DictWriter
#OBS:As chaves do dicionário devem ser as mesmas utilizadas no cabeçalho

from csv import DictWriter
with open('filmes2.csv', 'w') as arquivo: #substituir o w por a adiciona sem remover os dados ateriores
    cabecalho = (['Título', 'Gênero', 'Duração']) #cabeçalho
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme')
        if filme != 'sair':
            genero = input('Informe o gênero')
            duracao = input('Informe a duração em min')
            escritor_csv.writerow({'Título': filme,'Gênero': genero,'Duração': duracao}) #recebe um dicionário

