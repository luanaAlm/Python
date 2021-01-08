"""
Lendo arquivos CSV
CSV: Valores separados por vírgulas

#possivel de trabalhar porêm não iddeal
with open("lutadores.csv") as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    #print(type(dados))
    print(dados)

#Reader
from csv import reader
with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) #pula o cabeçalho
    for linha in leitor_csv:
        #cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} cm')

"""
#DictReader
from csv import DictReader
with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        #cada linha é uma lista
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['Pais']} e mede {linha['Altura (em cm)']}")




