#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''precisa baixar o arquivo mp3. e abrir no projeto'''
from pygame import mixer

#necessita-se iniciar o módulo
mixer.init()
mixer.music.load('exercicio21.mp3')
mixer.music.play()
input('Agora você escuta?')
'''
#Faça um programa em Python que abra e reproduza o áudio de um arquivo .mp3.
import mp3play
clip = mp3play.load(r'C:\gozar.mp3\gozar.mp3')
clip.play()
'''