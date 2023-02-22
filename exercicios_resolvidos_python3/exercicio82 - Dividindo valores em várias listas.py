"""
Crie um programa que vai ler VÁRIOS NÚMEROS  e colocar em uma LISTA.
Depois disso, crie DUAS LISTAS EXTRAS que vão conter apenas os valores PARES e os valores IMPARES
digitados, respectivamente.

Ao final, mostre o conteúdo dos TRÊS LISTAS geradas.
primeiro looping leitura dos valores
segundo looping analisa e coloca nas listas.
"""
listanum = []# list()
listnum_pares = []
listnum_impares = []
while True:
    num = int(input('Digite um valor: '))
    listanum.append(num)
    flag = str(input('Você deseja continuar [S/N]? '))
    if flag in 'Nn':
        break
for c in listanum:#for i, v in enumerate(listnum):
    if c % 2 == 0:
        listnum_pares.append(c)
    else:
        listnum_impares.append(c)
print(f'Os valores inseridos na lista 1 são: {listanum}')
print(f'Os valores pares são: {listnum_pares}')
print(f'Os valores impares são : {listnum_impares}')