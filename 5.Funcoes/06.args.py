"""
Entendendo o *args
É um parametro de entrada de uma função 
Onde pode ser chamado de qualquer coisa, porêm deve-se colocar o (*) no começo 
Ele coloca os valores extras informados como entrada como uma tuplas (que são imutáveis)
"""
# Entendendo o *args
def soma_todos_os_numeros(*args):
    return sum(args)

#Tuplas
print(soma_todos_os_numeros())
print(soma_todos_os_numeros(1))
print(soma_todos_os_numeros(2, 3))
print(soma_todos_os_numeros(2, 3, 4))
print(soma_todos_os_numeros(3.24, 4, 5, 6))

def verifica_informacao(*args):
    #verificandoo se geek e university estao contidos em args 
    if 'Geek' in args and 'university' in args:
        return 'bem-vindo!'
    return 'Eu não tenho certeza que é você!'

print(verifica_informacao())
print(verifica_informacao(1, True, 'university', 'Geek'))
print(verifica_informacao(1, 'university', 3.145))