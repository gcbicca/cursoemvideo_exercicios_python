"""
Crie um programa que tenha uma TUPLA única com NOMES DE PRODUTOS e seus respectivos PREÇOS, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma TABULAR.
"""
lista = ('Lápis', 1.75, 'Borracha', 2.0, 'Caderno', 15.90,
         'Estojo', 25.0, 'Trasferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('_' * 45)
l = 'LISTAGEM DE PREÇOS'
print(f'{l:^45}')
print('_' * 45)
for x in range(0, 17, 2):
    t = 30 - len(lista[x])
    print(f'{lista[x]}', '.' * t, f'R$ {lista[x+1]:>6}')
print('_' * 45)
