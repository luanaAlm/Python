# -*- coding: utf-8 -*-
"""
Escrevendo em arquivos

OBS1: Ao abrir o arquivo para leitura, não se pode realizar escrita nele;
    de mesma forma ao abrir o arquivo para escrita, não se pode realizar leitura
OBS2: Para escrevermos dados de um arquivo, após abrirmos o arquivo utilizamos a função
    write(), que recebe a string como parâmetro. caso contrário teremos TypeError

OBS3: Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado,
    caso ele ja exista, o anterior sera apagado e outro será criado, deste modo o conteúdo
    do antigo será perdido.
"""
#w: modo de escrita do arquivo
with open('teste1.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil\n')
    arquivo.write('Podemos colocar quantas linhas quisermos\n')
    arquivo.write('Mais essa é a ultima linha.\n')
