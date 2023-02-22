""" Elabore um programa que calcule o valor a ser pago por um produto considerando o seu PREÇO
NORMAL e CONDIÇÃO DE PAGAMENTO:
à vista DINHEIROO/CHEQUE: 10% de desconto
à vista no CARTÃO: 5% de desconto
em até 2x NO CARTÃO: preço normal
3x OU MAIS no cartão: 20% de juros
"""
print('{:=^40}'.format('\033[1;33m LOJAS BICCA\033[m ')) #A primeira parte do códio é para centralizar (:^40) e o = é para acrescentar os =.
preco_fix = float(input('Digite o valor do produto:R$'))
print("Escolha a condição de pagamento:\n"
                 "[1] à vista DINHEIRO/CHEQUE: 10% de desconto\n"
                 "[2] à vista no CARTÃO: 5% de desconto\n"
                 "[3] em até 2x no CARTÃO: Preço normal\n"
                 "[4] 3x ou mais no CARTÃO: 20% de juros")
opcao_pagamento = int(input('Opção: '))
if opcao_pagamento == 1:
    print(f'O produto com o preço de R${preco_fix}, na condição especial escolhida fica por apenas R${preco_fix - (preco_fix * 0.1)}')
elif opcao_pagamento == 2:
    print(f'O produto com o preço de R${preco_fix}, na condição especial escolhida fica por apenas R${preco_fix - (preco_fix * 0.05)}')
elif opcao_pagamento == 3:
    print(f'O produto irá custar no total R${preco_fix}\nAs parcelas ficaram R${preco_fix / 2} por mês.')
elif opcao_pagamento == 4:
    quant_parcelamento = int(input('Digite o número de parcelas que deseja (3 à 12): '))
    preco_juros = preco_fix + (preco_fix * 0.2)
    print(f'O produto com o preço de R${preco_fix}, nessas condições de pagamento irá custar no total R${preco_juros} COM JUROS.')
    print(f'Em {quant_parcelamento} vezes, as parcelas ficaram R${preco_juros / quant_parcelamento} por mês.')
else:
    print('\033[1;31mOpção inválida de pagamento. Tente novamente digitando uma opção válida.\033[m')
