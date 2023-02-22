'''
Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado
. O programa só vai parar quando o usuário digitar o valor 999
, que é a CONDIÇÃO DE PARADA. No final, mostre QUANTOS NÚMEROS
foram digitados e qual foi a SOMA entre eles
(Desconsiderando o flag).
'''
print('-'*30)
print('CALCULADORA DE NÚMEROS INTEIROS')
print('-'*30)
print('''O programa soma os números inteiros digitados e
exibi-os ao final mostrando o resultado da soma 
e a quantidade de números inteiros digitados.''')
print('Para sair do programa digite: 999')
cont = soma = c = 0
while c != 999:
    n = int(input('Digite um número inteiro: '))
    c = n
    if n != 999:
        soma = n + soma
        cont += 1
print(f'A soma dos números inteiros é {soma} e foi digitado {cont} números inteiros.')