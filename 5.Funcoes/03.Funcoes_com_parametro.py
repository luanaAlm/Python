"""
Funções com Parametro de entrada
Recebe dados para ser processado dentro delas
"""

#Refatorando um função: Forma 1
def quadrado(numero):
    return numero ** 2

#Forma 1
ret = quadrado(6)
print(ret)
#Forma 2"
print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

#Refatorando a função
def cantar_parabens(aniversariante):
    print("Parabens pra voce")
    print("Nessa data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")
    print(f"Viva o(a) {aniversariante} !")

cantar_parabens('João')

#varios paaramentros como entrada
def soma(a, b):
    return a+ b

def multiplica(num1, num2):
    return num1 * num2

def outra(num, b, msg):
    return (num + b) * msg

print('soma: ', soma(2,5))
print('Multiplicação: ', multiplica(4, 5))
print(outra(5,5,'pi '))

#nomeando parametros
def nome_completo(nome, sobrenome):
    return f'seu nome completo é: {nome} {sobrenome}'

print(nome_completo('Maria', 'Gorete'))

#Diferença entre parametros e argumentos
#parametros: sao variaveis declaradas na definiição de uma função (nome, sobrenome)
#Argumentos: são dados passados durante a excução de umaa função ('Maria', 'Gorete')

#Argumentos nomados (Keyword Arguments)
print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(sobrenome='Marques', nome='Mario'))

#erro ao ultilizar o return
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 !=0:
            total = total + num
    return total

lista = [1,2,3,4,5,6,7]
print(soma_impares(lista))

tupla = 1,2,3,4,5,6,7
print(soma_impares(tupla))