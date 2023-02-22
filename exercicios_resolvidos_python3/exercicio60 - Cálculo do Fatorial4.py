n = int(input('Digite o número que deseja realizar o fatorial: '))
cont = n
f = 1
print(f'Calculando o {n}!.')
for c in range(n, 0, -1):
    f = f * c
    print(c, 'x ' if c > 1 else '= ', end='')
print(f)
