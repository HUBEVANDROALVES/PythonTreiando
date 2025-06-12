import pygame
import time
pygame.init()
pygame.mixer.music.load('21play.mp3')
pygame.mixer.music.play()

time.sleep(10)

pygame.mixer.music.stop()
