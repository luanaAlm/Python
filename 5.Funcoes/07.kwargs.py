"""
**kwargs
Exige que se use parmetros nomeados o tranformando em um dicionário 
"""
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'a cor favorita de {pessoa.title()} e : {cor.title()}')

cores_favoritas(
    marcos = 'verde',
    julia = 'amarelo',
    fernanda = 'azul',
    vanessa = 'branco'
)

#Os parametros *args e **kwargs não sao obrigatorios