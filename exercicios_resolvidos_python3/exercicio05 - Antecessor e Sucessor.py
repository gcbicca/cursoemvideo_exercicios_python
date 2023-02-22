#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[1;33m',
         'cyan':'\033[1;36m',
         'purple':'\033[1;35m',
         'red':'\033[1;31m'}
n1 = int(input('\033[1;33mDigite um número: '))
n1_ant = n1 - 1
n1_suc = n1 + 1
print(f'\033[1;33mSeu número é\033[1;36m {n1}\033[1;33m sendo o seu antecessor\033[1;36m {n1_ant}\033[1;33m e seu sucessor\033[1;36m {n1_suc}')
'''
Dá para colocar sem as duas variáveis fazendo .format(n1, (n1-1), (n1+1))).
Utilizar dessa forma, faz economizar memório no dispositivo ,
pois não cria mais variáveis, entretanto,
se eu irei precisar da varial mais a frente necessirarei dela.
'''

