"""Crie um programa que faça o computador jogar JOKENPÔ com você."""
print('{:=^40}'.format(' \033[1;33mAlphaJOKENPÔ\033[m '))
import random
print('Vou ganhar de você no JOKENPÔ! HAHAHAHAH')
print('Escolha sua forma:\n'
                    '[1] PEDRA\n'
                    '[2] PAPEL\n'
                    '[3] TESOURA')

lista1 = ['PEDRA','PAPEL','TESOURA']
JOKENPO_CPU = random.randint(0, 2)
print(lista1[JOKENPO_CPU])
jokenpo = int(input('Opção: '))
JOKENPO = (lista1[jokenpo])
PEDRA = 1
PAPEL = 2
TESOURA = 3
lista = [PEDRA, PAPEL,TESOURA]
jokenpo_cpu = random.choice(lista)
if jokenpo == jokenpo_cpu:
    print('\033[1;33mEMPATE\033[m')
elif jokenpo == 1 and jokenpo_cpu == 3:
    print('\033[1;36mParabéns você ganhou!\033[m\nJogador: Pedra\nCPU: Tesoura')
elif jokenpo == 2 and jokenpo_cpu == 1:
    print('\033[1;36mParabéns você ganhou!\033[m\nJogador: Papel\nCPU: Pedra')
elif jokenpo == 3 and jokenpo_cpu == 2:
    print('\033[1;36mParabéns você ganhou!\033[m\nJogador: Tesoura\nCPU: Papel')
elif jokenpo == 1 and jokenpo_cpu == 2:
    print('\033[1;31mVocê perdeu!\033[m\nJogador: Pedra\nCPU: Papel')
elif jokenpo == 2 and jokenpo_cpu == 3:
    print('\033[1;31mVocê perdeu!\033[m\nJogador: Papel\nCPU: Tesoura')
elif jokenpo == 3 and jokenpo_cpu == 1:
    print('\033[1;31mVocê perdeu!\033[m\nJogador: Tesoura\nCPU: Pedra')
else:
    print('Jogada inválida! Tente novamente com uma alternativa válida')