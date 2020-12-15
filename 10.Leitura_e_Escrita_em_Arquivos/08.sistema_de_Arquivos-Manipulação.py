# -*- coding: utf-8 -*-
"""
Sistema de Arquivos - Manipulação
"""
import os
"""
#descobrindo se um arquivo ou diretorio existe
print(os.path.exists('arquivo.txt'))
print(os.path.exists('arquivo2.txt'))
print(os.path.exists('Python\\Tipos_de_Dados'))
print(os.path.exists('outro'))
"""

#Criando arquivos
open('arquivo-teste.txt', 'w').close()
#Deletar arquivo (OBS: eles nao irao para a lixeira)
os.remove('arquivo-teste.txt')
#Remover diretorios
#os.rmdir('')
"""
#removendo arvore de diretorios
for arquivos in os.scandir(''):
    print(f'- {arquivos.name}')
    if arquivos.is_file():
        os.remove(arquivos.path)
"""