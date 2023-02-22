#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$ 1.00 = R$3.27
nota_1 = int(input('Quantas notas de R$1: '))
nota_2 = int(input('Quantas notas de R$2: '))
nota_5 = int(input('Quantas notas de R$5: '))
nota_10 = int(input('Quantas notas de R$10: '))
nota_25 = int(input('Quantas notas de R$25: '))
nota_50 = int(input('Quantas notas de R$50: '))
nota_100 = int(input('Quantas notas de R$100: '))
dinheiro_carteira = (nota_1*1)+(nota_2*2)+(nota_5*5)+(nota_10*10)+(nota_25*25)+(nota_50*50)+(nota_100*100)
valor_dolar = 3.27
dinheiro_em_dolar = dinheiro_carteira // valor_dolar
sobra = dinheiro_carteira % valor_dolar
print('O valor que você tem na carteira é: R${} reais, sendo assim, você pode comprar US${} dólares. Sobrando R${} reais'.format(dinheiro_carteira,dinheiro_em_dolar,sobra))