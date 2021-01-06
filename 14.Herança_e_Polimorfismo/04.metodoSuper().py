"""
POO - Método Super() se refere a super classe
"""
class Animal():

    def __init__(self, nome, especie):
       self.__nome = nome
       self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} faz {som}')

class Gato(Animal):
    def __init__(self, nome, especie, raca):
        super(Gato, self).__init__(nome, especie)
        super().faz_som('auauauauauau') #acesso a qualquer elemento
        ##Outra forma
        #Animal.__init__(self, nome, especie)
        self.raca = raca

felix = Gato('felix', 'Felino', 'Angorá')
felix.faz_som('miau')