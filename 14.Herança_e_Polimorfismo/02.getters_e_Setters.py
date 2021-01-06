"""
Propriedades POO: Getters e Setters
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

    #Getters e Setters
    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('José', 3000, 5000)
conta2 = Conta('Marcos', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma dos saldos nas contas são {soma}')

print(conta1.__dict__)
conta1.set_limite(999999)
print(conta1.__dict__)