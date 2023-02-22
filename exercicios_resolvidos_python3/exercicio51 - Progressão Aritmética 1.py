num = int(input('\nDigite o Primeiro número da PA: '))
razão = int(input('Digite a Razão da PA: '))
for c in range(1, 11):
    print(num, end=' ')
    num += razão
print('Acabou')