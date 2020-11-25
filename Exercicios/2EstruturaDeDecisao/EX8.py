"""
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

#O método isalpha () verifica se a string consiste apenas em caracteres alfabéticos.
print("Em que turno você estuda?")
letra = input("DIgite M-matutino ou V-Vespertino ou N- Noturno")

if letra.isalpha():
    if letra =="m":
        print("Bom Dia!")
    elif letra == "t":
        print("Boa Tarde!")
    elif letra == "n":
        print("Boa Noite!")
else:
    print("Valor Inválido!")