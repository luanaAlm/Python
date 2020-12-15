# -*- coding: utf-8 -*-
"""
StringIO
"""
from io import StringIO
mensagem = 'Essa é uma string comum'

#Arquivo com texto
#Arquivo na memória
arquivo = StringIO(mensagem)
#arquivo = open('arquivo.txt', 'w')
print(arquivo.read())