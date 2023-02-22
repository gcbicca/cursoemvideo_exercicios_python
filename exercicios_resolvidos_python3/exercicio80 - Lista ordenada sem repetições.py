"""
Crie um programa onde o usuário possa digitar cinco VALORES NUMÉRICOS e cadastre-os em uma LISTA, JÁ NA POSIÇÃO CORRETA
inserção (sem usar o SORT()).
No final, mostre a LISTA ORDENADA na tela.
ex: 3..8...5 - Colocar no meio o número 5. pode usar o insirt/append/
"""
listanum = []
bigger = lower = 0
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0:
        bigger = lower = num
    if num >= bigger:
        listanum.append(num)
        print(f'O valor {num} foi adicionado ao final da lista!')
        bigger = num
    elif num <= lower:
        listanum.insert(0, num)
        print(f'O valor {num} foi adicionado ao início da lista!')
        lower = num
    else:
        for i in range(5):
            if num <= listanum[i]:
                listanum.insert(i, num)
                print(f'O número {num} foi adicionado na posição {i}.')
                break
print(f'A lista ordena fica: {listanum}')
