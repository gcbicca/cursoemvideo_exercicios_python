#Crie um script Python que leia dois números e tente mostrar a soma entre eles.
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[1;33m',
         'cyan':'\033[1;36m',
         'purple':'\033[1;35m',
         'red':'\033[1;31m'}
numero1 = int(input('\033[1;36mDigite o primeiro número da soma: '))
numero2 = int(input('\033[1;31mDigite o segundo número da soma:\033[m '))
soma = numero1+numero2
print('O resultado da soma de {}{}{} mais {}{}{} é: {}{}'.format(cores['cyan'], numero1, cores['limpa'], cores['red'], numero2, cores['limpa'], cores['amarelo'], soma))