"""
Atributos: Caracterissticas do objeto;
    É por ele que consegue-se representar computacionalmete os estados de um objeto

    Em python divide-se os atributis em 3 grupos:
        -Atributos de instância;
        -Atributos de classe;
        -Atributos dinâmicos;

-Atributos de instância: São atributos declarados dentro do metodo construtor
    (utilizado para a construção do objeto)

OBS: Em python por convensao ficou estabelecido que, todo atributo de uma classe é publico,
ou seja, pode ser acessado em todo o projeto.
"""
#Classes com aributos publicos

class Lampada:
    #Atributos de instância
    def __init__(self, voltagem, cor): #__init__ é um método construtor
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

#ps4 = Produto()

#Classe com atributos privados / uso do __ duplo underscode noo inicio do nome
# Conhecido tambem com Name Mangling
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_email(self):
        print(self.email)
    def mostra_senha(self):
        print(self.__senha)

user = Acesso('user@gmail.com', '12345')
print(user.email)

#print(user.__senha) #AttributeError
print(user._Acesso__senha) # Name Mangling, forma não convencional
print('\n')
print(user.email)
print(user.mostra_senha())

#Atributos de instância
# Ao criarmos uma instância/objetos de uma classe, todas as instâncias terao estes atributos

user1 = Acesso('aluno@gmail.com', '654654')
user2 = Acesso('professor@gmail.com', '32132')
print('\n')
user1.mostra_email()
user2.mostra_email()

#Atributos de classe
#São atributos que são declarados dentro da classe, ou seja fora dd construtor
#Geramente ja iniciamos um valor, e este é compartilhado entre todas as instâncias da classe, ou seja,
# ao invez de cada instância da classe ter seus próprios valores

#Refatorando aa classe Produto

class Produto:
    #Atributo de classe
    imposto = 1.05
    contador = 0
    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor + Produto.imposto)
        Produto.contador = self.id
print('\n')
p1 = Produto('PS 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.valor) #Acesso não convencional
print(p2.valor)
print(Produto.imposto) #Acesso correto
print(p1.id)
print(p2.id)

#Atributos Dinâmicos -> podem ser criados em tempo de execulção
#Ele é exclusivo da instância que o criou
p1 = Produto('Arroz', 'Alimento', 22)
p2 = Produto('Sal', 'Alimento', 1)
p2.peso = '5kg'
print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

print(p1.__dict__)
print(p2.__dict__)
print(Produto.__dict__)

del p2.peso

print(p1.__dict__)
print(p2.__dict__)
