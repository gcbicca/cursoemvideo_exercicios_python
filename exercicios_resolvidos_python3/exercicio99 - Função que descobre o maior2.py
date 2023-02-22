"""Faça um programa que tenha uma FUNÇÃO chamada MAIOR(), que receba vários PARÂMETROS com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual dele é o MAIOR."""


# Essa função irá receber vários parâmetros e um número arbitrário de argumentos.
def maior(*numeros):
    cont = maior = 0
    print('Analisando os valores passados...')
    for c in numeros:
        print(f'{c}', end=' ')
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        cont += 1
    if cont == 0:
        print('Nenhum valor foi passado, insira novamente outro valor!')
    else:
        print(f' | O maior valor passado foi {maior}.')
        print(f'Foram passados {cont} números ao todo.')
        print('~' * 50)


# Programa Principal
maior(1, 2, 4, 6)
maior(1)
maior(2, 8)
maior(0)
maior()
