""" A Confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 25 anos: SÊNIOR
Acima: MASTER
"""
from datetime import date
ano_atual = date.today().year
print('\033[1;33mCadastramento de atletas da Confederação Nacional de Natação\033[m')
ano_nasc = int(input('Digite o ano de nascimento do atleta com 4 dígitos: '))
idade = ano_atual - ano_nasc
if idade <= 9:
    print(f'O atleta tem {idade} anos e se enquadra na categoria MIRIM')
elif idade >=10 and idade <= 14:# Dá para tirar a parte do 10 e deixar só o 14 pq, o python já passou pelo if anterior, portanto, n tem idade infeiror a isso
    print(f'O atleta tem {idade} anos e se enquadra na categoria INFANTIL')
elif idade >= 15 and idade <= 19:
    print(f'O atleta tem {idade} anos e se enquadra na categoria JUNIOR')
elif idade >= 20 and idade <= 25:
    print(f'O atleta tem {idade} anos e se enquadra na categoria SÊNIOR')
else:
    print(f'O atleta tem {idade} anos e se enquadra na categoria MASTER')
