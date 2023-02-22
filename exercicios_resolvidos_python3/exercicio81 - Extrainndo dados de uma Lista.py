"""
Crie um programa que vai ler VÁRIOS NÚMEROS e colocar em uma LISTA.
Depois disso, mostre:
a) QUANTOS números foram digitados.
b) A lista de valores, ordenada de forma DECRESCENTE.
c) Se o valor 5 foi digitado e está ou não na LISTA.
"""
listnum= []
while True:
    num = int(input('Digite um valor:'))#listnum.append(int(input('XXXX')))
    listnum.append(num)
    flag = str(input('Você deseja continuar [S/N]? '))
    if flag in 'Nn':
        break
if 5 in listnum:
    print('O valor 5 está presente na lista de valores')
else:
    print('O valor 5 não está presente na lista de valores')
print(f'Os valores obtidos são : {listnum}')
print(f'A quantidade de número inseridos na lista são {len(listnum)}')
listnum.sort(reverse=True)
print(f'A lista de valores ordenada em ordem decrescente fica {listnum}')#{f'Os valores decrescente foram {sorted(listnum, reverse = True}
