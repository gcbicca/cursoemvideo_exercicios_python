'''
Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule
um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''
salario = float(input('Digite o seu salário em R$: '))
aumento_10 = (salario * 0.10) + salario
aumento_15 = (salario * 0.15) + salario
if salario > 1250.00:
    print('O seu aumento foi de R${}'.format(aumento_10))
else:
    print('O seu aumento foi de R${}'.format(aumento_15))
#aumento = salario + (salario * 10 / 100)
#print('Q seu salário com o reajuste é R${:.2f}'.format(aumento))