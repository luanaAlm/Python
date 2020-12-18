"""
Geradores (generators): são interators
    - podem ser criados com funções geradoras
    - funções geradoras utilizam a palavra yield
    - generators functios utiliza o yield
    - generators functios utiliza o yield multiplas vezes
    - generators functios retorna um generators
"""

# Ex generators functios
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

gen = conta_ate(100)
"""
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""

for num in gen:
    print(num)