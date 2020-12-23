"""
Propriedades POO: Properties
"""
class Conta:
    contador = 0
    def __init__(self, titular, saldo, limite):
        self.__titular