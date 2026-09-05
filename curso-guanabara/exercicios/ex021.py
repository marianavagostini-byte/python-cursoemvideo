# ex021 - Tocando um MP3
# Fonte: Curso em Vídeo - desafio oficial (complementado)

# Requer: pip install pygame  +  um arquivo de áudio 'ex021.mp3' na mesma pasta
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input('Tocando... pressione ENTER para encerrar.')
pygame.mixer.music.stop()
