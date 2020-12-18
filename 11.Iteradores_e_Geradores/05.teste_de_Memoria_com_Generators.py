"""
Teste de Memória com Generators
"""
#consome mais mamória
def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

"""
#teste
for n in fib_list(100000):
    print(n)
"""
#consome menos mamória
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

for n in fib_gen(100000):
    print(n)