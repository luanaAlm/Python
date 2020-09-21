"""
Dicionarios tambem conhecidos como mapas
São coleçoes do tipo chave/valor
Dicionarios são representados por chaves

print(type({}))
"""


print('Forma 1')
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(type(paises))
print(paises)

print('-----')
print('Forma 2')
paises = dict(br = 'Brasil', eua = 'Estados Unidos', py = 'Paraguai')
print(type(paises))
print(paises)


print('-----')
print('Acessando via chave')
print(paises['br'])
print(paises['eua'])
print(paises['py'])
print('-----')

print('-- Forma 1--')

pais = paises.get('br')
if pais:
    print(f'encontrei: {pais}')
else:
    print('nao encontrei o pais')

print('-- Forma 2 --')
# pais = paises.get('ru', 'Não encontrado')
print(pais)

print('--- Usando qualquer tipo de dado ---')
localidades = {
    (35.2564, 35.5684): "Escritório no Rio de Janeiro",
    (25.9856, 35.0014): "Escritório em Pernanbuco",
    (40.9964, 39.6284): "Escritório no Alabama",
}
print(type(localidades))
print(localidades)

receita = {'jan' : 100, 'fev' : 120, 'mar' : 300}
print(receita)
receita['abr'] = 350
print(receita)
novo_dado = {'mai':500}
receita.update(novo_dado)
print(receita)
print('Formna 1 de atualizar ')
receita['mai'] = 550
print(receita)
print('Formna 2 de atualizar ')
receita.update({'mai': 600})
print(receita)

print('--- Remover dados do dicionario ---')
print('Forma 1')
ret = receita.pop('mar')
print(receita)
print(ret)
print('Forma 2')
del receita['fev']
print(receita)

print('--- Carrinho - LIST---')
carrinho = []
produto1 = ['playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
print(type(carrinho))

print('\n--- Carrinho - TUPLE---')

produto1 = ('playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)
carrinho = (produto1, produto2)

print(carrinho)
print(type(carrinho))

print('\n--- Carrinho - DICIONARIO---')

carrinho = []
produto1 = {'nome': 'playstation 4', 'quantidade': 1, 'valor': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'valor': 150.00}
carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
print(type(carrinho))

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

print('\nCopiando um diconario para o outro')
print('\ndeep copy')
novo = d.copy()
print(novo)
print('novo valor')
novo['d'] = 4
print(novo)
print('\nShallow copy')
novo = d
print(novo)
novo['d'] = 5
print(d)
print(novo)

print('\nlimpeza')
d.clear()
print(d)