"""
Propriedades POO: Properties
"""
#classe contritora
class Conta:
    contador = 0
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    #Métodos
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
conta2 = Conta('Marcos', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f'A soma dos saldos nas contas são {soma}')

print(conta1.__dict__)
conta1.limite = 76852
print(conta1.__dict__)