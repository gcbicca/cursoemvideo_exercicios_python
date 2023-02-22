'''
Crie um programa que mostre na tela TODOS OS NÚMEROS PARES ques
estão no intervalo entre 1 e 50.
'''
for c in range (0,50+2,2):# (2, 51 , 2)
    if c % 2 == 0:
        print(c) # end= ' ' serve para tirar os espaços
print('fim')