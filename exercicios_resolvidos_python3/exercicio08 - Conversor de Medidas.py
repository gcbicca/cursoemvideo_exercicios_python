#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
metros = float(input('Digite uma distância em metros: '))
metros_dm = int(metros * 10)
metros_cent = int(metros * 100)
metros_mili = int(metros * 1000)
metros_decametro = int(metros / 10)
metros_hectometro = int(metros / 100)
metros_quilometro = float(metros / 1000)
print('O seu valor em metros é: {}m. \nEm Decímetros é: {}dm \nEsse número convertido em centímetros é: {}cm. \nEm milimetros é: {}mm'.format(metros, metros_dm, metros_cent, metros_mili))
print('A distãncia em metros escolhida foi: {}m. \nEssa distância em Decâmetros é: {}dam \nA distância em Hectômetro é: {}hm \nE em Quilômetros a distância é: {}km'.format(metros, metros_decametro, metros_hectometro, metros_quilometro))
