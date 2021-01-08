"""
Escrevendo em arquivos CSV
write() -> escrever
writerow() -> Escreve ma linha
"""
from csv import writer

with open('filmes.csv', 'w', encoding='UTF-8') as arquivo:
    escritor_csv = writer(arquivo)
