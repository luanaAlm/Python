"""
Herança
    Reaproveitamento de código
    Extenção de Classes

    --- OBS ---
    A partir de uma classe existente, nós extendemos outra classe que passa a herdar
    atributos e métodos da classe herdada
    Sobrescrita (Overriding): Ocorre quando reescrevemos/reimprementamos um método presente na
    super classe
"""
#Super classe - classe Mãe - classe Pai - classe Base
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'Nome: {self.__nome} {self.__sobrenome} \nCPF: {self.__cpf}'

#Sub classe - classe filha - classe especifica
class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) #Forma1 -> não comum de acessas a super classe
        self.__renda = renda

    #Sobrescrita (Overriding)
    def nome_completo(self):
        print(f'-- Cliente --')
        print(super().nome_completo())
        return f'Renda: {self.__renda}'

class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf) #Forma2 -> Forma comum de acessas a super classe
        self.__matricula = matricula

    #Sobrescrita (Overriding)
    def nome_completo(self):
        print(f'-- Funcionário --')
        print(super().nome_completo())
        return f'Matricula: {self.__matricula}'

cliente1 = Cliente('Maria', 'Joaquina', '123.456.789-22', 20000)
func1 = Funcionario('Sofia', 'Sousa', '987.654.321.99', 12345)


print(cliente1.nome_completo())
#print(cliente1.__dict__)
print(func1.nome_completo())
#print(func1.__dict__)
