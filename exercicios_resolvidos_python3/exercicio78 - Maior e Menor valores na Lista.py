"""
Faça um programa que leia 5 VALORES NUMÉRICOS  e guarde-os em uma LISTA. for com range
No final, mostre qual foi o MAIOR e o MENOR valor digitado e as suas respectivas POSIÇÕES na lista.
ex: Digite um valor para a posiçao 0,1,2,3,4
pode ter mais de um número na mesma posição
"""
lista = []
p_bigger = []
p_lower = []
for c in range(0,5):
    num = int(input(f'Digite um valor na posição {c}: '))
    lista.append(num)
for i, v in enumerate(lista):
    if v == max(lista):
        p_bigger.append(i)
    if v == min(lista):
        p_lower.append(i)
print(f'Os valores digitados foram {lista}')
print(f'Os menores valores foram {min(lista)} nas posições {p_lower}')
print(f'Os maiores valores foram {max(lista)} nas posições {p_bigger}')