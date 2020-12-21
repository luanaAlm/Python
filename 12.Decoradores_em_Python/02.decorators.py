"""
Decorators
    -São funções
    -Envolve outras funções e e aprimoram seus comportamentos
"""
#Decorators com sintaxe Sugar
def seja_educado(funcao):
    def educado():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return educado

@seja_educado
def apresentando():
    print('Meu nome é Pedro')

apresentando()

@seja_educado
def quero_dormir():
    print('Quero dormir ...')

quero_dormir()