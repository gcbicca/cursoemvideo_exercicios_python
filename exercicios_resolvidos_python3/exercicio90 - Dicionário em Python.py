"""
Faça um programa que leia NOME E MÉDIA de um aluno, guardando também a SITUAÇÃO em um DICIONÁRIO. No
final, mostre o conteúdo da estrutura na tela.
"""
dataset = {}
name = str(input('Name: ')).strip().title()
#dataset['name'] = str(input('name: '))
dataset['Name'] = name
average = float(input(f'Average of {name}: '))
dataset['Average'] = average
if average >= 6:
    dataset['Current_situation'] = 'Approved'
else:
    dataset['Current_situation'] = 'Disapproved'
for k, v in dataset.items():#.items me da os valores de key and values
    print(f'{k} equals {v}')
