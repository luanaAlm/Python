"""
Métodos Mágicos: são todos os métodos que utilizam dunder

dunder init -> __init__()
Dunder > duplo Underscore

dunder repr> serve para representar objetos
def __repr__(self):
    return f'{self.titulo} escrito por {self.autor} e contêm {self.paginas} páginas'

dunder str> retorna uma representação de string de um objeto.
def __str__(self):
    return self.titulo

dunder del> deleta
def __del__(self):
        print('livro foi deletado da memoria')

"""

class Livro():
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __len__(self):
        return self.paginas

    def __add__(self, other):
        return f'{self.titulo} - {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Não pssp multiplicar'

livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)
print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)

print(livro1 * 3)