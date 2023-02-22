#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preço_produto_normal = float(input('Qual é o precesso do seu produto? R$:'))
desconto_produto = (5 / 100)
valor_desconto = (preço_produto_normal * desconto_produto)
preço_produto_promo = preço_produto_normal - valor_desconto
print('O preço do seu produto sem desconto é R${} \nO produto na promo com 5% vai custar R${}'.format(preço_produto_normal, preço_produto_promo))
#Uma forma diferente de escrever de maneira mais fácil é
'''
novo = preço_produto_normal - (preço_produto_normal*5/100)
'''
