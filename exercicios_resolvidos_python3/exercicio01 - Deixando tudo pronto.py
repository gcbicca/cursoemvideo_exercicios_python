#Exercício Python #001 - Imprimir a mensagem Olá mundo!
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[1;33m',
         'cyan':'\033[1;36m',
         'purple':'\033[1;35m',
         }
msg = 'Olá, Mundo!'
print('{}{}{}'.format(cores['amarelo'], msg, cores['limpa']))