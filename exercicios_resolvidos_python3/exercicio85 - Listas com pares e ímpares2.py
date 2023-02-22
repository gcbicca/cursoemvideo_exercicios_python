list = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0: #Numero par
        list[0].append(num)
    elif num % 2 == 1: #Numero impar
        list[1].append(num)
list[0].sort()
list[1].sort()
print(f'Os valores ordenados na lista de pares é {list[0]}')
print(f'Os valores ordenados na lista de ímpares é {list[1]}')