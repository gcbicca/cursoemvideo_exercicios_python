'''
Faça um programa que leia um NÚMERO qualquer e mostre o seu
FATORIAL.

Ex:
5! = 5x4x3x2x1 = 120
'''
n1 = int(input('Digite um número que deseja realizar o FATORIAL: '))
c = 999999 # Desnecessário pois a variável mudará na próxima linha
c = n1
print(f'Calculando {n1}!.')
while c > 0: #Usa o maior nesse caso é melhor c > 0: pois chegará até 1
    c -= 1
    if c == n1 -1:
        fatorial = c * n1
    else:
        fatorial = c * fatorial
        print(c, f' x')
print(fatorial)