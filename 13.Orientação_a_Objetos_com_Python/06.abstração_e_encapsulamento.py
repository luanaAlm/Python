"""
Abstração e Encapsulamento
Abstração: é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e
métodos privados de usuário
"""
class Conta:
    contador = 400
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Titular: {self.__titular} \nSaldo: {self.__saldo} \nLimite: {self.__limite}\n----')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')

    def tranferir(self, valor, conta_destino):
        #remover valor da conta de origem
        self.__saldo -= valor
        #adicionar valor na conta de destino
        conta_destino.__saldo += valor
#Testando
conta1 = Conta('Geek', 150, 1500)
conta2 = Conta('Angelina', 300, 2000)
"""
print(conta1.__dict__)
conta1.depositar(150)
print(conta1.__dict__)
conta1.sacar(200)
print(conta1.__dict__)
"""
conta2.tranferir(100, conta1)
conta1.extrato()
conta2.extrato()