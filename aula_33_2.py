"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = input("Que horas é agora? ")
horas_int = int(horas)

if horas_int >= 0 and horas_int <= 11:
    print("Bom dia!")
elif horas_int >= 12 and horas_int <= 17:
    print("Boa tarde!")
elif horas_int >= 18 and horas_int <= 23:
    print("Boa noite!")
else:
    print("Você não digitou um numero entre 0 e 23")