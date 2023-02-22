"""
Crie um programa que leia o NOME e o PREÇO de VÁRIOS PRODUTOS.
O programa deverá perguntar se o USUÁRIO vai continuar. No final,
mostre:
A) qual é o TOTAL GASTO na compra;
B) quantos produtos custam MAIS de R$1000;
C) qual é o NOME do produto mais BARATO.
"""
tot = onek = smaller = cont = 0
smallername = ' '
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto em R$'))
    tot = tot + preco
    cont += 1
    if preco > 1000:
        onek = onek + 1
    if cont == 1 or preco < smaller:#Solução para evitar o 9999 e a simplificação de mais um IF
        smaller = preco
        smallername = nome
    flag = ' '
    while flag not in 'SN':
        flag = str(input('Você deseja continuar? [S]im ou [N]ão: ')).strip().upper()[0]
    if flag == 'N':
        break
print(f'O total gasto na compra foi R${tot}')
print(f'Um total de {onek} produtos custam mais de R$1000.')
print(f'O nome do produto mais barato é: {smallername}.')