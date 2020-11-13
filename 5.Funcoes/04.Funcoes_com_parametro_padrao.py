"""
Funções com parametro padrão (Default Paramters)
A passagem de parametros é opsional
Pode-se usar qualquer tipo de dado
"""

print("Exemplo de passagem de parametro obrigatória")
def quadrado(numero):
    return numero ** 2

print(quadrado(1))
#print(quadrado()) TypeErro

#valor padrão no parametro potencia, na ausencia de numer de entrada em sempre usará o 2 definido na potencia
#obs: os paremetros com valor defaut (padrão) devem sempre estaano final da declaração, se nao da erro
def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2,3))
print(exponencial(3)) #por padrão sera elevado ao quadrado

#Exemplo 1
def mostra_informacao(nome='Geek', instrutor = False):
    if nome == 'Geek' and instrutor:
        return f'Bem-vindo {nome}'
    elif nome == 'Geek':
        return 'Não é o instrutor'
    return f'ola {nome}'

print(mostra_informacao())
print(mostra_informacao('Geek'))
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True)) #sera atribuido ao 1 parametro
print(mostra_informacao('Maria'))

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2,3))
print(mat(2,2,subtracao))