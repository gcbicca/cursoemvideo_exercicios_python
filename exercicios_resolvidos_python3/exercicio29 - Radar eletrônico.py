'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R%7.00 por cada Km acima do limite.
'''
vel_carro = float(input('Digite a velocidade do carro em Km/h: '))
multa = (vel_carro - 80) * 7
if vel_carro > 80.0:
    print('Você foi multado, diminua a velocidade! Sua multa chegará nos próximos meses em sua casa')
    print('A sua multa chegará no valor de R${:.2f}'.format(multa))


