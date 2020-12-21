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