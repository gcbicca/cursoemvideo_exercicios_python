""" Faça um programa que leia o PESO de CINCO PESSOAS. No final,
 mostre qual foi o MAIOR e o MENOR peso lidos."""
contador_bigger = 0
bigger = 0
contador_smaller = 1000000
smaller = 0.0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pesssoa: '))
    if peso > contador_bigger:
        bigger = peso
        contador_bigger = peso
    if peso < contador_smaller:
        smaller = peso
        contador_smaller = peso
print(bigger, smaller)
