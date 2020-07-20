"""
Estruturas lógicas
end - or - not - is
"""
ativo = True
logado = True

#AND e OR todos os valores precisam ser True
print('AND')
if ativo and logado:
    print('Usuário ativo no sistema')
else:
    print('Voce preoisa ativar sua conta')

print('OR')
if ativo or logado:
    print('Usuário ativo no sistema')
else:
    print('Voce preoisa ativar sua conta')

#NOT valor booleano é invertido, se for true vira falso e vice-versa
ativado = True
logar = False
print('NOT')
if not ativado:
    print('Voce preoisa ativar sua conta')
else:
    print('bem-vindo usuario')
print('-----')
print(not False)
print(not True)

print('IS')
if ativo is False:
    print('Usuário ativo no sistema')
else:
    print('Voce preoisa ativar sua conta')
