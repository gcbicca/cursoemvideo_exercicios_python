""" Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e
mostra a soma apenas daqueles que forem PARES. Se o valor digitado for ÍMPAR, desconsidere-o.
"""
cont = 0
soma = 0
for n in range(1, 7):
    num = int(input(f'Digite o {n}°: '))
    if num % 2 == 0:
        cont += 1
        soma += num
if cont == 1:
    print(f'Você informou apenas {cont} número PAR, portanto o resutado é {soma}')
else:
    print(f'Você informou {cont} números PARES que somados resultam em {soma}.')