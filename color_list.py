import pygame

pygame.init()


for name, rgba in pygame.color.THECOLORS.items():
    print(f"{name}: {rgba}")