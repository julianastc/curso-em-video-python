import pygame

pygame.init()
pygame.mixer.init()

som = pygame.mixer.music.load("lanadelrey.mp3")

pygame.mixer.music.play()
input()
pygame.event.wait()