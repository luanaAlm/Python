"""
São funçõoes sem nome ou seja função anônimas


def funcao(x):
    return 3 * x + 1
print(funcao(7))
print(funcao(4))

#Expressao lambda
print('-- Lambda --')
calc = lambda x: 3 * x + 1
print(calc(7))
print(calc(4))

#lambda com varias entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('maria', 'sousa'))
print(nome_completo('FERNANDA     ', 'soares'))

#em funções python podemos ter nenhuma ou varis entradas. em lambda tmb
amar = lambda : 'Como não amar python'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * 5) ** 0.5
tres = lambda x, y, z: 3 / (1/ x + 1 / y + 1 / z)
#n = lambda x1, x2, ..., xn: <expressão>
print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))
"""
#Outros exxemplos
nomes = ['Isaac Asivon', 'Marcos Vinicios', 'Gorete V. Lacerda', 'Lazaro Sousa', 'Maria O. C. Vilani',
           'Julioc Cesar', 'H. G. Cruz', 'Reinaldo Maraes', 'Daniel Marques', 'Heitor Enzo']
print(nomes)
nomes.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(nomes)