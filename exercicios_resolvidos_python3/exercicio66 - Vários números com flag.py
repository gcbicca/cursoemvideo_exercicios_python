"""
Crie um programa que leia VÁRIOS NÚMEROS INTEIROS pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a CONDIÇÃO DE PARADA. No final, mostre QUANTOS NÚMEROS
foram digitados e qual foi a SOMA entre eles(desconsiderando o flag).
"""
soma = cont = 0
while True: #Loop infinito
    n = int(input('Digite um número inteiro: '))
    if n == 999: #Condição que caso o número for 999 o loop irá interromper(loop infinito)
        break
    cont += 1 #Contador para somar o número da variável quantidade de números somados.
    soma += n #Contador que realiza a soma dos números digitados.
print(f'Foram computados {cont} números e a soma entre eles resultou em {soma}.')
