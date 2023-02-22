"""
Crie um programa onde o usuário possa digitar SETE VALORES NUMÉRICOS e cadastre-os
em uma LISTA ÚNICA que mantenha separads os valores PARES e ÍMPARES. No final,
mostre os valores pares e impares em ordem CRESCENTES.
"""
temppar = []
tempimpar = []
lista = []
for c in range(0, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:# O número é par
        temppar.append(num)
    elif num % 2 ==1:# O número é impar
        tempimpar.append(num)
tempimpar.sort()# Ordena a lista de impar
temppar.sort()# Ordena a lista de par
lista.append(tempimpar[:])
lista.append(temppar[:])
print(lista)