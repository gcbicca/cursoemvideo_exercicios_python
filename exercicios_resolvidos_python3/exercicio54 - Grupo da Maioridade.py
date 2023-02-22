""" Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""
from datetime import date
adult = 0
kid = 0
for c in range(0, 7):
    cont += 1
    ano = int(input(f'Digite o ano de nascimento da  {c}ª pessoa: '))
    idade = date.today().year - ano
    if idade >= 18:
        adult += 1
    else:
        kid += 1
print(f'O número de pessoas na maioridade é {adult}, já na menor idade é {kid}.')
