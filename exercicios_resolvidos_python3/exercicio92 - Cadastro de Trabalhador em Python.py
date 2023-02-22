"""
Crie um programa que leia NOME, ANO DE NASCIMENTO e CARTEIRA DE TRABALHO e cadastre-os (com IDADE)
em um DICIONÁRIO se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ANO DE
CONTRATAÇÃO e o SALÁRIO. Calcule e acrescente, além da IDADE, com quantos anos a pessoa se APOSENTAR.
#35 ANOS DE COTRIIBUIÇÃO
"""
from datetime import date
dataset = {}
dataset['name'] = str(input('Name: ')).strip().title()
dataset['year_of_birth'] = int(input('Year of birth: '))
dataset['age'] = date.today().year - dataset['year_of_birth']#datatime.now().year
dataset['work_card'] = int(input('Work card (if you dont have it enter 0): '))
if dataset['work_card'] != 0:
    dataset['year_hired'] = int(input('Year of hiring your first job: '))
    dataset['salary'] = float(input('Salary:'))
    dataset['retirement'] = dataset['year_hired'] + 35 - dataset['year_of_birth']
    # contratação + 35 - ano atual + idade
print('-=' * 10)
print('  == DATA ==  ')
print('-=' * 10)
for k, v in dataset.items():
    print(f'   - {k} equals {v}')
    print('-=' * 20)
print(dataset)