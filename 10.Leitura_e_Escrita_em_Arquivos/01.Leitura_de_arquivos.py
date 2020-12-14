"""
Leitura de arquivos
Para ler o arquivo usa-se a função open()
"""
arquivo = open('teste.txt')
#print(arquivo)
#print(type(arquivo))

#para ler um arquivo é necessário, aós aberto, usar a função read()
#print(arquivo.read())
ret = arquivo.read()
print(type(ret))
print(ret)
