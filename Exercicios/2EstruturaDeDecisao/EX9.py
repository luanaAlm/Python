"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
salario = float(input("Digite o salario: "))
print(f"salário antes do reajuste: {salario}")
if salario <= 280:
    calc = (salario * 20) / 100
    soma = salario + calc
    print("percentual de aumento aplicado:", 20,'%')
    print(f"o valor do aumento: {calc}")
    print(f"o novo salário, após o aumento: {soma}")
elif (salario > 280) and (salario < 1500):
    calc = (salario * 15) / 100
    soma = salario + calc
    print("percentual de aumento aplicado:", 15, '%')
    print(f"o valor do aumento: {calc}")
    print(f"o novo salário, após o aumento: {soma}")
elif salario > 1500:
    calc = (salario * 5) / 100
    soma = salario + calc
    print("percentual de aumento aplicado:", 5, '%')
    print(f"o valor do aumento: {calc}")
    print(f"o novo salário, após o aumento: {soma}")


