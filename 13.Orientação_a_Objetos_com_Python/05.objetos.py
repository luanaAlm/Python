"""
Objetos são instâncias de classes. Ou seja após o mapeamento do objeto do mundo real para a sua
representação computacional, devemos poder criar quantos objetos forem necesários.
Podemos pensar nos objetos/instância de uma classe como variáveis do tipo definido na classe.
"""

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True
class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi!')

class ContaCorrente:
    contador = 499
    def __init__(self, limite, saldo, Cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = Cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é o {self.__cliente._Cliente__nome}')

class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


"""
#Instâncias/Objetos -> lamp1
lamp1 = Lampada('Branca', 110, 60)
lamp1.ligar_desligar()
lamp1.ligar_desligar()

print(f'A lampada está ligada? {lamp1.checa_lampada()}')
cc1 = ContaCorrente(5000, 20000)
user1 = Usuario('Felicity', 'Jones', 'fe@gmail.com', '123456')
"""
cliente1 = Cliente('Angelina Jolie', '123.456.789-99')
cc = ContaCorrente(5000, 10000, cliente1)
cc.mostra_cliente()
cc._ContaCorrente__cliente.diz()