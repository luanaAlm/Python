"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
"""
print("-----")
print("-----")

print("-----")


"""
nome = str(input("Digite seu nome"))
while len(nome) <= 3:
    nome = str(input("Nome nenor que 3 caracteres digite novamente: "))

idade=int(input("Digite a idade"))
while ( idade > 150 or idade < 0 ):
    idade = int(input("Idade invalida digite novamente "))

salario=float(input("Digite o salario"))
while salario < 0:
    salario = float(input("salario invalido digite novamente "))

sexo = str(input("Digite o sexo\n"))
while sexo !="f" and sexo !="m":
	sexo=str(input("valor invalido informe o sexo novamente "))

estCiv = str(input("Digite o seu estado civil\n"))
while (estCiv !="s" and estCiv !="c" and estCiv !="v" and estCiv != "d"):
	estCiv=str(input("valor invalido"))

print(f'Bem-vindo(a)\nnome: {nome}')
print(f'idade: {idade}')
print(f'Salario: {salario}')
print(f'sexo: {sexo}')
print(f'Estado civil: {estCiv}')


