"""
Teste de Velocidade com Expressões Geradoras
"""
"""
#geradores
def nums():
     for num in range(1, 10):
         yield num

gen1 = nums()

print(gen1)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))


gen2 = (num for num in range(1, 10))
print(gen2)
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
"""
#teste de velocidade
import time
gen_inicio = time.time()
print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio

#Teste list comprehension
list_inicio = time.time()
print(sum([num for num in range(100000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator expression levou {gen_tempo}')
print('\n')
print(f'list comprehension levou {list_tempo}')
