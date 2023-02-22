lista = ('Lápis', 1.75, 'Borracha', 2.0, 'Caderno', 15.90,
         'Estojo', 25.0, 'Trasferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('_' * 45)
print(f'{"LISTAGEM DE PREÇOS":^40}')#Utilizando o " para diferenciar e :^40 centralizar com 40 espaços
print('_' * 45)
for x in range(0, 17, 2):
    print(f'{lista[x]:.<30}', f'R$ {lista[x+1]:>6.2f}')#:.<30 alinhado a direita com . e 30 espaços
#:>6.2f alinhado a esquerda com 6 espaços e o número com 2 float
print('_' * 45)