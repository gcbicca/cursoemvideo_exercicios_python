""" Desenvolva um programa que leia o PRIMEIRO TERMO
e a RAZÃO de uma PA. No final, mostre os 10 primeiros termos dessa progressão. """
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 0
print(f'O primeiro termo da PA é {a1}.\n'
      f'A razão escolhida foi {r}.\n'
      f'Os 10 primeiro termos dessa Progressão Aritmética são:\n{a1}')

for c in range(1, 9+1):
    cont += 1
    print(f'{a1 + cont * r}')

'''
num = int(input('\nDigite o Primeiro número da PA: '))
razão = int(input('Digite a Razão da PA: '))
for c in range(1, 11):
    print(num, end=' ')
    num += razão
print('Acabou')
'''
