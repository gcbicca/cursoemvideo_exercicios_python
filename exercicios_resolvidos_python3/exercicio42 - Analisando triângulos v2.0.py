""" Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
de mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais
ESCALENO: todos os lados diferentes
"""
print('\033[1;36m-=-\033[m'*20)
print('\033[1;33mAnalisador de Triângulos v2.0\033[m')
print('\033[1;36m-=-\033[m'*20)
lado_a = float(input('Digite o comprimento do lado A do triângulo: '))
lado_b = float(input('Digite o comprimento do lado B do triângulo: '))
lado_c = float(input('Digite o comprimento do lado C do triângulo: '))
if lado_a < lado_b + lado_c and lado_b < lado_c + lado_a and lado_c < lado_b + lado_a:
    print('Um triângulo pode ser formado e ele é ', end='')
    if lado_a == lado_b == lado_c: #utilizando apenas as variaveis e sinais de ==
        print('EQUILÁTERO')
    elif lado_a != lado_b != lado_c != lado_a:#necessita-se fazer a verificação do lado c com o lado a
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Com esses segmentos não se pode formar um triângulo.')
'''modulo_b_c = lado_b % lado_c
modulo_a_c = lado_a % lado_c
modulo_a_b = lado_a % lado_b
print('Caso as três condições abaixo sejam verdadeiras, o resultado é que pode existir um triâgulo.\nQuando uma condição não obedece a regra não é possível existir um triângulo.')
if modulo_b_c < lado_a and modulo_b_c < lado_b + lado_c:
    print('O teste da condição B e C é Verdadeira')
    teste_b_c = ('Verdadeiro')
else:
    print('O teste da condição B e C é Falsa')
if modulo_a_c < lado_b and modulo_a_c < lado_a + lado_c:
    print('O teste da condição A e C é Verdadeira')
    teste_a_c = ('Verdadeiro')
else:
    print('O teste da condição A e C é Falsa')

if modulo_a_b < lado_c and modulo_a_b < lado_a + lado_b:
    print('O teste da condição A e B é Verdadeira')
    teste_a_b = ('Verdadeiro')
else:
    print('O teste da condição A e B é Falsa')'''
#Teste para ver que tipo de triângulo é
'''if teste_a_b == 'Verdadeiro' and teste_a_c == 'Verdadeiro' and teste_b_c == 'Verdadeiro':
    print('As condições são todas Verdadeiras!')
else:
    print('As codições não foram atendidas e não se pode formar um triângulo.')
    exit()'''
"""if lado_a == lado_b and lado_a == lado_c:
    print('Parabéns! O seu triângulo foi formado e ele é um triângulo EQUILÁTERO.')
elif lado_a == lado_b or lado_a == lado_c:
    print('Parabéns! O seu triângulo foi formado e ele é um triângulo ISÓCELES.')
elif lado_a != lado_b and lado_b != lado_c and lado_a != lado_c:
    print('Parabéns! O seu triângulo foi formado e ele é um triângulo ESCALENO.')"""