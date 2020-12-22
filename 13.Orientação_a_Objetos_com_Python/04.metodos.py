"""
Métodos são funções e são oss comportamentos do objeto
podem ser:
    -Métodos de instância
    -Métodos de classe

OBS:
    __init__ é um método construtor
    Os método/Funções dunder em python são chamados de métodos mágicos
    Métodos sao scritos com letras minusculas ou com _
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

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0
    @classmethod #Usa-se quando não se acesso aos atributos
    def conta_usuarios(cls): #cls prórpia classe
        print(f'temos {cls.contador} usuario(s) no sistema')

    #metodos estaticos
    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        #self.__senha = cryp.hash(senha, round=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario(a) criado: {self.__sobrenome}')
    #Metodos de instãncia sao criados quando precisa-se acessas atributos
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def gera_usuario(self):
        return self.__email.split('@')[0]

"""
p1 = Produto('PS 4', 'Video Game', 2300)
print(p1.desconto(10))
print(Produto.desconto(p1, 15)) #self, desconto

user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '124565')
user2 = Usuario('Marcos', 'Aurélio', 'marcos@gmail.com', '64665')

print(Usuario.nome_completo(user1))
print(f'senha: {user1._Usuario__senha}')
print(user2.nome_completo())
print(f'senha: {user2._Usuario__senha}')

nome = input('Informe o nome')
sobrenome = input('Informe o nome')
email = input('Informe o email')
senha = input('Inform a senha')
confirma_senha = input('Confirme a senha')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha errada')
print('Usuário criado com sucesso')

senha = input('Inform a senha')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acess negado')

print(f'Senha User criptografada: {user._Usuario__senha}')

user3 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '124565')
user4 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '124565')

Usuario.conta_usuarios()

user5 = Usuario('Maria', 'Joaquina', 'mariaJo@gmail.com', '124565')
print(user5._Usuario__gera_usuario())
"""

print(Usuario.contador)
print(Usuario.definicao())
user6 = Usuario('Maria', 'Joaquina', 'mariaJo@gmail.com', '124565')
print(user6.contador)
print(user6.definicao())
