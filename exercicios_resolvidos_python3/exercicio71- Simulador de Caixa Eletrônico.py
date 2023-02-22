"""
Crie um programa que simule o funcionamento de um CAIXA ELETRÔNICO.
No inicio, pergunte ao usuário qual será o VALOR A SER SACADO (número
inteiro) e o programa vai informar quantas CÉDULAS de cada valor serão
entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$2O, R$10 e R$1.
"""
xfifty = xtwenty = xten = xone = 0
saque = int(input('Digite o valor que deseja sacar (Número inteiro) em R$'))
if saque % 50 == 0:
    xfifty = saque / 50
    print(f'Seu saque será de R${saque} e será entregue {xfifty} notas de R$50.')
elif saque % 50 != 0:
    xfifty = saque
    xtwenty = xfifty % 50
    xfifty = saque // 50
    print(f'Número de notas de R$50: {xfifty:.0f}')
if xtwenty % 20 == 0:
    xtwenty = xtwenty / 20
    print(f'Número de notas de R$20: {xtwenty:.0f}')
elif xtwenty % 20 != 0:
    xten = xtwenty % 20
    xtwenty = xtwenty // 20
    print(f'Número de notas de R$20: {xtwenty:.0f}')
if xten % 10 == 0:
    xten = xten / 10
    print(f'Número de notas de R$10: {xten:.0f}')
elif xten % 10 != 0:
    xone = xten % 10
    xten = xten // 10
    print(f'Número de notas de R$10: {xten:.0f}')
if xone % 1 == 0:
    xone = xone / 1
    print(f'Número de notas de R$1: {xone:.0f}')
print('Fim do programa')