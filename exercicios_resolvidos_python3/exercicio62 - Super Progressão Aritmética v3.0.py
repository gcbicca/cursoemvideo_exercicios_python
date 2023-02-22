'''
Melhore o DESAFIO 61, perguntando para o usuário se ele
quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 TERMOS.
'''
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da Progressão Aritmética: '))
c = 10
xtermos = 0
while c != 0:
    print(a1,'→ ' if c > 1 else 'FIM',  end='')
    a1 += r
    if c == 1:
        print('\nVocê gostaria de acrescentar mais termos?')
        c = int(input('Se sim, digite quantos, se não digite [0]: ')) + 1
    c -= 1
    xtermos += 1
print(f'A Progressão Artimética foi finalizada com {xtermos} termos.')
print('Fim do programa!')
