"""
Escopo de variaveis
1- globais: seu escopo compreende a todo o programa
# 2- local: reconhecida somente no bloco onde foi declarada
"""

# variavel global
numero = 42
print(numero)

# variavel local (bloco)
if numero >10:
    novo = numero +10
    print(novo)