"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
#O método isalpha () verifica se a string consiste apenas em caracteres alfabéticos.
letra = input("Informe uma letra ou consoante:")

if letra.isalpha():
    if letra =="a":
        print("Vogal")
    elif letra == "e":
        print("Vogal")
    elif letra == "i":
        print("Vogal")
    elif letra == "o":
        print("Vogal")
    elif letra == "u":
        print("Vogal")
    else:
        print("Consoante")
else:
    print("Não é uma letra!")