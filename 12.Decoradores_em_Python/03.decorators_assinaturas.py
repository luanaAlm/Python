"""
Decorators assinaturas
"""

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'olá eu sou o(a) {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Eu gostaria de pedir {principal}, acompanhado de {acompanhamento}'

print(saudacao('Daniel'))
print(ordenar('pizza', 'suco'))

@gritar
def lol():
    return 'lol'

print(lol())

#parametros nomeados
print(ordenar(acompanhamento='Batata Frita', principal='Picanha'))

#Decorators com argumentos
def verifica_primeiro_argumento(valor):
    def interna(funcao): #função decorada
        def outra(*args, **kwargsf): #funcao de validacao
            if args and args[0] != valor:
                return f'valor incorreto, primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargsf)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

print(soma_dez(10, 12))
print(soma_dez(1, 22))

print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('maria isabel', 'cuz cuz'))