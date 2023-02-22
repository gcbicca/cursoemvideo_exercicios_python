# Output Quantos dias o carro foi alugado?
# Quantos Km rodados?
# O total a pagar pelo aluguel é de R$
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$0.15 por Km rodado.
dias_alugados = float(input('Por quantos dias o carro foi alugado? '))
km_rodados = float(input('Quantos Km foram rodados com o carro durante os dias de aluguel? '))
total_a_pagar = (dias_alugados * 60) + (km_rodados * 0.15)
print('A quantidade de dias de aluguem foram: {} dias e a quantidade de Km rodados foram: {} Km \nO total a pagar é: R${:.2f}'.format(dias_alugados, km_rodados, total_a_pagar))
