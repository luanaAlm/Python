"""
Seek(): usadas para movimmentar o cursos pelo arquivo
Cursors():
"""
"""

arquivo = open('teste.txt')
print(arquivo.read())
print('\n')
arquivo.seek(400)
print(arquivo.read())
print('\n')
#readline(): ler o arquivo linha a linha
print(arquivo.readline())

linhas = arquivo.readlines()
print(len(linhas))
"""
#abrir uma conexao com o disco do pc
arquivo = open('teste.txt')