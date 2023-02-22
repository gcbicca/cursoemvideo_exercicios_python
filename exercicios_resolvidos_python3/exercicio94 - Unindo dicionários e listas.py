"""
Crie um programa que leia NOME, SEXO e IDADE de VÁRIAS PESSOAS, guardando os dados de cada pessoa em um DICIONÁRIO
e todos os dicionários em uma LISTA. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A MÉDIA de idade do grupo.
C) Uma lista com todas as MULHERES.
D) Uma lista com todas as pessoas com IDADE acima da MÉDIA.
"""
dataset = []
age = []
woman = []
older = []
while True:
    people = {}
    people['name'] = str(input('Name: ')).strip().title()
    people['age'] = int(input('Age: '))
    while True:
        people['sex'] = str(input('Sex [M/F]: ')).strip().upper()[0]
        if people['sex'] not in 'MF':
            print('ERROR! Please enter only M or F.')
        else:
            break
    if people['sex'] == 'F':
        woman.append(people['name'])
    age. append(people['age'])
    dataset.append(people)#.append(people.copy())
    del people
    while True:
        flag = str(input('Do you want to continue [Y/N]: ')).strip().upper()[0]
        if flag in 'YN':
            break
        print('ERROR! Please enter only Y or N.')
    if flag in 'N':
            break
    print('=-' * 15)
mean = sum(age)/len(dataset)
"""for i, v in enumerate(dataset):
    for k, value in v.items():
        if k == 'age':
            if value > mean:
                older.append(v['name'])"""
print('=-' * 20)
print('    == DATA ==    ')
print('=-'*20)
print(f'The number of people registered is {len(dataset)}.')
print(f'The mean of the group is {mean}')
print(f'The name of all women is {woman}')
print(f'The name of all people older than average is: ')
for p in dataset:
    if p['age'] > mean:
        older.append(p['name'])
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
