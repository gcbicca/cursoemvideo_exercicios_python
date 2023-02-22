# Exercício Python #002 - Respondendo ao Usuário
# Escreva um program que recebe o nome e escreva uma mensagem de boas-vindas
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[1;33m',
         'cyan':'\033[1;36m',
         'purple':'\033[1;35m',
         }
nome = input('Qual é o seu nome? ')
print('\033[1;36mSeja bem-vindo, {}{}!'.format(cores['amarelo'], nome))

