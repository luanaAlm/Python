"""
Métodos são funções e são oss comportamentos do objeto
podem ser:
    -Métodos de instância
    -Métodos de classe

OBS:
    __init__ é um método construtor
    Os método/Funções dunder em python são chamados de métodos mágicos
"""

#Métodos de instância
class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999
    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0
    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

class Usuario:
    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    def __correr__(self, metros):
        print(f'{self.__nome} esta correndo {metros} metros')