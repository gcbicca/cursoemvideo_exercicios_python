"""
Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de ZERO até VINTE.

Seu programa deverá ler um número pelo teclado (ENTRE 0 E 20) e motrá-lo por EXTENSO.
EX: Digite um número entre 0 e 20. não pode mais que 20 ou números negativos.
saída = você digitou o número treze.
"""
seq = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove','dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número de 0 a 20: '))
        if 0 <= n <= 20:
            break
    print(f'O número digitado foi {n} e o número escrito de forma por extenso é: {seq[n]} ')
    flag = ' '
    while flag not in 'SN':
        flag = str(input('Digite [S]im para continuar e [N]ão para parar: ')).strip().upper()[0]
    if flag == 'N':
        break


"""while True:
    n = int(input('Digite um número de 0 a 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ', end='')"""