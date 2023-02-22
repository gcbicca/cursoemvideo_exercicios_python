#Crie um algoritmo que leia um número e mostre o seu dobro triplo e raiz quadrada
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[1;33m',
         'cyan':'\033[1;36m',
         'purple':'\033[1;35m',
         'red':'\033[1;31m'}
n = int(input('\033[1;33mDigite um número inteiro: '))
n_dup = n * 2
n_tri = n * 3
n_raiz = n**(1/2)
print(f'O número inteiro escolhido foi: \033[1;36m{n}. \n\033[1;33mO seu dobro é: \033[1;36m{n_dup}.\n\033[1;33mO triplo é \033[1;36m{n_tri}.\n\033[1;33mA raiz é: \033[1;36m{n_raiz}')
#Posso excluir as variáveis com calculos e colocá-los nos prints
#print('O número inteiro escolhido foi: {}. \nO seu dobro é: {}. \nO triplo é {}. \n A raiz é: {:.2f}'.format(n, (n*2), (n*3), (n**(1/2))
#Outra forma de executar a raiz quadrada é pow(n(1/2))

#Utilizar dentro da máscara {} {:.2f} irá utilizar só duas casas decimais após a vírgula.

