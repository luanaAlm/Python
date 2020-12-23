"""
Propriedades POO: Properties
"""
class Conta:
    contador = 0
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Titular: {self.__titular} \nSaldo: {self.__saldo} '

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def trasferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

conta1 = Conta('José', 3000, 5000)
conta2 = Conta('Marcos', )