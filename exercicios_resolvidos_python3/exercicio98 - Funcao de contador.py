"""
Faça um programa que tenha uma FUNÇÃO chamada CONTADOR(), que receba trê PARÂMETROS:
INÍCIO, FIM, e PASSO e realize a contagem.
Seu programa tem que realizar TRÊS CONTAGENS através da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem Personalizada.
"""
from time import sleep


# Esse programa irá realizar contagens e receberá 3 parâmetros
def contador(inicio, fim, passo):
    """Esse programa irá mostrar os números de um sequência, tendo como parâmetros início, fim, passo. """
    print('~' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        print('ERROR! Você digitou o passo como 0.\nTente novamente com outro número. ')
    else:
        if passo < 0:
            passo *= -1
        if inicio < fim:
            cont = [n for n in range(inicio, fim+1, passo)]
            for v in cont:
                print(f'{v}', end=' ')
            print('FIM!')
        if fim < inicio:
            cont = [n for n in range(inicio, fim-1, -passo)]
            for i in cont:
                print(f'{i}', end=' ')
            print('FIM!')
# Defino uma variável e chamo a função para os seguintes argumentos.
contador(1, 10, 1)
contador(10, 0, 1)

# Peço para o usuário inserir uma contagem Personalizada
print('Agora é a sua vez de personalizar a Contagem!')
start = int(input('Início: '))
end = int(input('Fim: '))
pace = int(input('Passo: '))
contador(start, end, pace)
