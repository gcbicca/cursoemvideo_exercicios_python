n = int(input('Digite um número que deseja fazer o Fatorial: '))
c = n
f = 1
print(f'Calculando {n}!.')
while c > 0:
    '''print(f'{c} ', end='')
    print(f' x ' if c > 1 else ' = ', end='')'''
    print(c, 'x ' if c > 1 else '= ', end='')
    f = f * c
    c -= 1
print(f'{f}')

