import pygame
pygame.mixer.init()
pygame.mixer.music.load('faustao.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()