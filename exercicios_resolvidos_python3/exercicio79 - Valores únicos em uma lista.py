"""
Crie um programa onde o usuário possa digitar vários VALORES NUMÉRICOS e cadastre-os em uma LISTA.
Caso o número já exista lá dentro, ele NÃO SERÁ ADICIONADO. No final, serão exibidos todos os
VALORES ÚNICOS digitados, em ORDEM CRESCENTE.
ex: Digite um valor (INFINITAMENTE)
quer continuar? [S/N]
valor duplicado. não vou adicionar
"""
listanum = []
while True:
    num = int(input('Digite um valor: '))
    if num in listanum:#Posso utilizar o not in tbm!
        print('O número é duplicado!')
    else:
        listanum.append(num)
    flag = str(input('Você deseja continuar? [S]im ou [N]ão: ')).strip().upper()[0]
    if flag == 'N':#If flag in 'Nn'
        break
print(f'Os valores digitado foram: {listanum}')
listanum.sort()
print(f'Os valors digitado em ordem crescente são {listanum}')