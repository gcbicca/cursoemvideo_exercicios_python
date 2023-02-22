'''
Desenvolva um programa que pergunte a distância de uma
viagem em Km. Calcule o preço da pessagem cobrando R$0.50
por Km para viagens de até 200 Km e R$0.45 para viagens mais longas.
'''
dist_km = float(input('Qual foi a distância da viagem em Km: '))
preç_200 = dist_km * 0.50
preç_201 = dist_km * 0.45
#preço = dist_km * 0.50 if dist_km <= 200 else dist_km * 0.45
if dist_km <= 200.0:
    print('A distância da viagem foi de {} Km, sendo o valor da passagem de R${:.2f}'.format(dist_km, preç_200))
else:
    print('A distância da viagem foi de {} Km, sendo o valor da passagem de R${:.2f}'.format(dist_km, preç_201))
#print('O vaor da passagem R${:.2f}'.format(dist_km*0.50))

