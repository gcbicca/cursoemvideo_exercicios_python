'''
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
'''
print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
lado_a = float(input('Digite o comprimento de um lado do triângulo: '))
lado_b = float(input('Digite o comprimento do lado b do triângulo: '))
lado_c = float(input('Digite o comprimento do lado c do triângulo: '))
modulo_b_c = lado_b % lado_c
modulo_a_c = lado_a % lado_c
modulo_a_b = lado_a % lado_b
print('Caso as três condições abaixo sejam verdadeiras, o resultado é que pode existir um triâgulo.\nQuando uma condição não obedece a regra não é possível existir um triângulo.')
if modulo_b_c < lado_a and modulo_b_c < lado_b + lado_c:
    teste_b_c = ('Verdadeiro')
    print('O teste da condição B e C é Verdadeira')
else:
    teste_b_c = ('Falso')
    print('O teste da condição B e C é Falsa')
if modulo_a_c < lado_b and modulo_a_c < lado_a + lado_c:
    teste_a_c = ('Verdadeiro')
    print('O teste da condição A e C é Verdadeira')
else:
    print('O teste da condição A e C é Falsa')
if modulo_a_b < lado_c and modulo_a_b < lado_a + lado_b:
    teste_a_b = ('Vedadeiro')
    print('O teste da condição A e B é Verdadeira')
else:
    print('O teste da condição A e B é Falsa')
#if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b


