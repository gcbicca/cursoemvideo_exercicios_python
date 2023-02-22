""" Escreva um programa para aprovar o empréstimo
bancário para a compra de uma casa. O programa vai perguntar
o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS
ele vai pagar."""
''' Calcule o valor da pestação mensal, sabendo que ela não 
pode exceder 30% do salário ou então o empréstimo será negado.'''
valor_casa = float(input('Qual é o valor da casa que o senhor(a) pretende comprar? R$'))
salario = float(input('Qual é o valor do salário que o senhor(a) recebe? R$'))
temp_pagamento = int(input('Em quantos anos o senhor(a) pretende pagar? '))
prestacao_mensal = valor_casa / (temp_pagamento * 12)
print(f'Para pagar um casa no valor de R${valor_casa:.0f} em {temp_pagamento} anos,\nO valor das prestações mensais serão de R${prestacao_mensal:.2f}.')
if prestacao_mensal > (salario * 0.3):
    print('Seu empréstimo foi negado, devido ao valor mensal da prestação exceder 30% do seu salário.')
elif prestacao_mensal <= (salario * 0.3):
    print(f'Seu empréstimo foi aceito, o valor das parcelas serão R${prestacao_mensal:.2f}.')

"""# APROVADOR DE IMPRÉSTIMO V1.0

vhome = float(input('Digite o valor da casa: R$'))  # Valor da casa
sal = float(input('Digite seu salário mensal: R$'))  # Valor do Salário
years = int(input('Digite em quantos anos você deseja pagar a casa: '))  # Anos em que quer pagar a casa
phome = (vhome / (years * 12))  # Prestação mensal
sal30 = ((sal * 30) / 100)  # 30% do salário
cores = {'uncolor': '\033[m',  # Paleta de cores
         'red': '\033[31m',
         'blue': '\033[34m',
         'white': '\033[30m',
         'yellow': '\033[33m'}
if phome > sal30:  # Se a prestação mensal for maior que 30% do salário, então:
    print(f"{cores['white']}O seu pedido de impréstimo foi{cores['uncolor']} "
          f"{cores['red']}NEGADO{cores['white']}!{cores['uncolor']}")  # O Seu pedido de impréstimo foi NEGADO
else:
    print(f"{cores['white']}O seu pedido de impréstimo foi{cores['uncolor']} "
          f"{cores['blue']}ACEITO{cores['white']}!{cores['uncolor']}")  # O seu pedido de impréstimo foi ACEITO

print(f"{cores['white']}Para pagar uma casa de{cores['uncolor']} "
      f"{cores['yellow']}R${vhome:.2f}{cores['uncolor']} em {cores['white']}{years} anos, a prestação "
      f"será de{cores['uncolor']} "
      f"{cores['yellow']}R${phome:.2f}{cores['uncolor']} "
      f"{cores['white']}mensais.{cores['uncolor']}")

# This exercise was done by: Heitor :)"""