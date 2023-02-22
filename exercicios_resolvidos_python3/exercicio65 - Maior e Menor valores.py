'''
Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado
. No final da execução, mostre a MÉDIA ENTRE TODOS os valores
e qual foi o MAIOR e o MENOR valores lidos. O programa deve
perguntar ao usuário se ele quer ou não CONTINUAR a digitar
valores.
'''
print('-'*30)
print('ANALISADOR DE NÚMEROS INTEIROS')
print('-'*30)
p = ''
c = soma = maior = 0
menor = 999999999999999
"""
Pode ser usado para atribuir o valor a menor, não precisando colocar um
número gigante para menor.
if c == 1:
    maior = menor = n 
"""
while p != 'N':
    n = int(input('Digite um número inteiro: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma = n + soma
    c += 1
    print('-'*60)
    p = str(input('Digite [S] para continuar a digitar e [N] para parar o programa: ')).upper().strip()[0]
    print('-' * 60)
    if p == 'N':
        med = soma / c
print('~'*60)
print(f'Com {c} números inteiros digitados a Média foi de {med}.\nSoma {soma}. \nO Maior {maior}. \nO Menor {menor}.\nFim do Programa')