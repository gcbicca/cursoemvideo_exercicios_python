'''
Crie um programa que leia DOIS VALORES  e mostre um MENU na
tela:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada
caso
'''
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('====== MENU ======')
print('[1] Somar\n'
'[2] Multiplicar\n'
'[3] Maior\n'
'[4] Novos números\n'
'[5] Sair do programa')
out = False
while not out:
    menu = int(input('Digite qual ação do MENU você deseja: '))
    if menu == 1:
        somar = n1 + n2
        print(f'A soma de {n1} + {n2} = {somar}')
    elif menu == 2:
        multiplicar = n1 * n2
        print(f'O número {n1} x {n2} = {multiplicar}')
    elif menu == 3:
        if n1 > n2:
            maior = n1
            print(f'O maior número é {maior}')
        elif n1 < n2:
            maior = n2
            print(f'O maior número é {maior}')
        else:
            print('Os números são iguais.')
    elif menu == 4:
        n1 = int(input('Digite um novo valor para o primeiro número: '))
        n2 = int(input('Digite um novo valor para o segundo número: '))
    elif menu == 5:
        out = True

