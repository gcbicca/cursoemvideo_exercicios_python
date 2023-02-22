#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR
n_int = int(input('Digite um número inteiro: '))
n_par_impar = n_int % 2
if n_par_impar == 0:
    print('O número inteiro {} é PAR'.format(n_int))
else:
    print('O número inteiro {} é ÍMPAR'.format(n_int))

