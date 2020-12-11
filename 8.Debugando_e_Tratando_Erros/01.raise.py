"""
raise: lança exceções
- ele é uma palavra reservada
- com ele é possivel criar suas próprias exceções e mensagens de erro
"""
"""
raise ValueError('Valor incorreto')
"""
def colore(texto, cor):
    cores= ('verde', 'vermelho', 'amarelo', 'azul')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'texto: {texto}\n cor: {cor}')

colore('coração','roxo\n')
colore(1,2)
