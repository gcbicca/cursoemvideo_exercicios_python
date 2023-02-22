#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
#Ordem de precedência!
nota1 = float(input('Digite a nota do GA: '))
nota2 = float(input('Digite a nota do GB: '))
soma_nota = float(nota1 + nota2)
media_nota = float(nota1 + nota2)/2
print('A sua nota no GA foi de: {} pontos, no GB: {} pontos, a soma das suas notas foram: {} pontos e sua média final foi de: {:.2f} pontos.'.format(nota1,nota2,soma_nota,media_nota))
if media_nota>= 6:
    print('Parabéns você foi aprovado')
elif media_nota< 6:
    print('Infelizmente você foi reprovado')
