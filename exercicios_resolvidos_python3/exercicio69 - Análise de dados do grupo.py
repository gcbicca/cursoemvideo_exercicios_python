"""
Crie um programa que leia a IDADE e o SEXO de VÁRIAS PESSOAS.
A cada pessoa cadastrada, o programa deverá perguntar se o USUÁRIO
quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 ANOS;
B) quantos HOMENS foram castrados;
C) quantas MULHERES tem menos de 20 ANOS.
"""
qidade = qhomens = qmulheres20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Digite seu sexo [Masculino] ou [Feminino]: ')).strip().upper()[0]
    if idade > 18:
        qidade = qidade + 1
    if sex == 'M':
        qhomens = qhomens + 1
    if sex == 'F' and idade < 20:
        qmulheres20 = qmulheres20 + 1
    flag = ' '
    while flag not in 'SN':
        flag = str(input('Você deseja continuar? Digite [S] para Continuar e [N] para Parar: ')).strip().upper()[0]
    if flag == 'N':
        break
print("Dados coletados")
print(f'Número de pessoas maiores de 18 anos: {qidade}.')
print(f'Número de homens cadastrados: {qhomens}.')
print(f'Número de mulheres com menos de 20 anos: {qmulheres20}')
