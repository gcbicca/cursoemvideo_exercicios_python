#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta pinta uma área de 2m**2
largura_parede = float(input('Quantos metros tem a largura da parede?'))
altura_parede = float(input('Quantos metros tem a altura da parede?'))
area_parede = float(largura_parede * altura_parede) #Resultado vai ser dado em metros quadrados
quantidade_tinta = (area_parede / 2) #Resultado vai ser dado em litros
print('Sua parede tem a dimensão de {}x{} e sua área é de: {}m metros quadrados \nVocê vai precisar de {} litros de tinta para pintá-la.'.format(largura_parede, altura_parede, area_parede, quantidade_tinta))

