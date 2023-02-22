"""
Faça um programa que leia NOME E PESO de VÁRIAS PESSOAS, guardando tudo em uma LISTA.
No final, mostre:
a) QUANTAS pessoas foram cadastradas.
b) Uma listagem com as pessoas mais PESADAS.
c) Uma listagem com as pessoas mais LEVES.
"""
list = []
listfat = []
listthin = []
cont = bigger = lower = 0
while True:
    nome = str(input('Nome: '))
    list.append(nome)
    peso = float(input('Peso: '))
    list.append(peso)
    flag = str(input('Quer continuar [S/N]: ')).strip()[0]
    cont += 1
    if cont == 1:
        bigger = lower = peso
    if peso > bigger:
        bigger = peso
    elif peso < lower:
        lower = peso
    if flag in 'Nn':
        break
for pos, item in enumerate(list):
    val = isinstance(item, float)
    if val == True:
        if item == bigger:
            listfat.append(list[pos - 1])
        elif item == lower:
            listthin.append(list[pos - 1])
print(f'O número de pessoas cadastradas é {cont}')
print(f'O menor peso registrado foi {lower}. A lista de pessoas mais magras é {listthin}')
print(f'O maior peso registrado foi {bigger}. A lista de pessoas mais gordas é {listfat}')
