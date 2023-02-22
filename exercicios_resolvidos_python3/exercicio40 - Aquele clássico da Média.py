""" Crie um programa que e leia duas notas de um aluno e calcule sua média
mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO
"""
nota1 = float(input('Digite o valor da sua primeira nota: '))
nota2 = float(input('Digite o valor da sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Você foi REPROVADO! Sua média é {media:.2f}. Se esforce mais na próxima vez!')
elif media >= 5.0 and media <= 6.9:
    print(f'Você está de RECUPERAÇÃO! Sua média é {media:.2f}. Continue se esforçando para atingir uma nota favorável!')
elif media > 6.9:
    print(f'Você foi APROVADO! Sua média é {media:.2f}. Continue se esforçando para manter boas notas!')