'''
Faça um programa que leia uma frase pelo teclado e mostre:
-Quantas vezes aparece a letra 'A'
-Em que posição ela aparece a primeira vez.
-Em que posição aparece a últime vez.
'''
frase = str(input('Digite uma frase: ')).strip()
frase_upper = frase.upper()
frase_count_a = frase_upper.count('A')
frase_find_a_first = frase_upper.find('A')
frase_find_a_last = frase_upper.rfind('A')
print('A frase digitada foi: {}'.format(frase))
print('A quantidade de vezes que aparece a letra A é: {}, ela aparece pela primeira vez na posição {} e a última na posição {}'.format(frase_count_a, frase_find_a_first,frase_find_a_last))
'''
frase = str(input('Digite uma frase: ').strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra A aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra A aparece a última vez na posição {}'.format(frase.rfind('A')+1))
'''