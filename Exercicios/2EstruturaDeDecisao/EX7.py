"""
Faça um programa que pergunte o preço de três produtos
e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""
prod1 = float(input("Digite o valor do 1° produto:"))
prod2 = float(input("Digite o valor do 2° produto:"))
prod3 = float(input("Digite o valor do 3° produto:"))
if prod1 < prod2 and prod3:
    print("O menor valor é", prod1)
elif prod2 < prod1 and prod3:
    print("O menor valor é", prod2)
elif prod3 < prod1 and prod2:
    print("O menor valor é", prod3)