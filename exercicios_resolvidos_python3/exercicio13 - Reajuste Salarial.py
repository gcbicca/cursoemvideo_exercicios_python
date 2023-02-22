#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario_atual = float(input('Qual é o seu salário atual? R$'))
salario_reajuste = salario_atual + (salario_atual*15/100)
print('O seu salário atual de R${} reais, ele foi reajustado com 15% de aumento para R${} reais.'.format(salario_atual, salario_reajuste))
      
