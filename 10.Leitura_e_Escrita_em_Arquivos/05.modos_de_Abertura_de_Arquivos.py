# -*- coding: utf-8 -*-
"""
Modos de Abertura de Arquivos
'r' : Abre para leitura - padr�o
'r+' : Abre para o modo de atualização: leitura e escrita
'w' : Abre para escrita - sobrescreve caso o arquivo j� exista
'x' : Abre para escrita somente se o arquivo nao existir
'a' : Abre para escrita e adiciona o novo conteudo no final do arquivo
"""
"""
#Exemplo x
with open('teste2.txt', 'x') as arquivo:
    arquivo.write('Teste de conte�do. \n')
    
"""
#Exemplo a
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Infore uma fruta ou digite sair')
        if fruta !='sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

"""
#Exemplo r+
import os, sys
with open('teste1.txt', 'r+',) as arquivo:
    arquivo.seek(0)
    arquivo.write('No topo!\n')
    arquivo.write('Nova linha\n')
    arquivo.write('Mais uma linha\n')
"""