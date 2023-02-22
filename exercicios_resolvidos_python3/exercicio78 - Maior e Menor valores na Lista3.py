listanum= []
bigger = 0
lower = 0
for c in range(0,5):
    num = int(input(f'Digite um valor na posição {c}: '))
    listanum.append(num)
    if c == 0:
        bigger = lower = num
    else:
        if num > bigger:
            bigger = num
        if num < lower:
            lower = num
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi o {bigger} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == bigger:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi o {lower} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == lower:
        print(f'{i}... ', end='')
