# Desafio #004Faça um programa que leia algo pelo teclado o seu tipo primitivo e todas as informações possíveis sobre ela.
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[1;33m',
         'cyan':'\033[1;36m',
         'purple':'\033[1;35m',
         'red':'\033[1;31m'}
tipo_variavel = input('\033[1;36mDigite algo:\033[m ')
print(f'\033[1;33mA variável é do tipo primitivo:\033[m {type(tipo_variavel)}')
print(f'\033[1;33mA variável é Alfabética:\033[m {tipo_variavel.isalpha()}')
print(f'\033[1;33mA variável é Numérica:\033[m {tipo_variavel.isnumeric()}')
print(f'\033[1;33mA variável é Numérica ou Alfabética:\033[m {tipo_variavel.isalnum()}')
print(f'\033[1;33mA variável possue todas as letras maiúsculas:\033[m {tipo_variavel.isupper()}')
print(f'\033[1;33mA variável possue todas as letras minúsculas:\033[m {tipo_variavel.islower()}')
print(f'\033[1;33mA variável só tem espaços:\033[m {tipo_variavel.isspace()}')
print(f'\033[1;33mA variável está capitalizada:\033[m {tipo_variavel.istitle()}')