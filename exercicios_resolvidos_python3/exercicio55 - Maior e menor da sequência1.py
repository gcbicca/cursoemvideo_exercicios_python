bigger = 0
smaller = 100000
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pesssoa: '))
    if peso > bigger:
        bigger = peso
    if peso < smaller:
        smaller = peso
print(f'O maior peso foi {bigger}kg.\n'
      f'O menor peso foi {smaller}kg.')