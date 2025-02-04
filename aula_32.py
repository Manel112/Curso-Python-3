"""
Flag (Bandeira) - Marcar um local
None = não valor
is e is not = é ou não é (tipo, valor, idedntidade)
id = Identidade
"""

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')