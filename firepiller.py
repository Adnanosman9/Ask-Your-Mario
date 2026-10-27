import pygame
import random

# W, H = 900, 520

# orange = pygame.Color("orange")
# yellow = pygame.Color("yellow")
# gray = pygame.Color("grey")
# white = pygame.Color("white")

# Ground = 390


class firepillar:
    def __init__(self, wx):
        self.wx = wx
        self.h = random.randint(40,75)
        self.frame = 0
        self.flame_offset = 0


    def draw(self, surf, cam):
        self.frame += 1
        if self.frame % 6 == 0:
            self.flame_offset = random.randint(-3, 3)

            sx = self.wx - cam
            if not (-55 < sx < W + 55):
                return

            pygame.draw.rect(surf, gray, (sx - 10, Ground - self.h, 20, self.h))
            pygame.draw.rect(surf, pygame.Color("gray3"), (sx - 10, Ground - self.h, 20, self.h), 2)

            flame_y = Ground - self.h + self.flame_offset

            pygame.draw.ellipse(surf, pygame.Color("red3"), (sx - 9, flame_y - 16, 18, 20))
            pygame.draw.ellipse(surf, orange, (sx - 7, flame_y - 24, 14, 20))
            pygame.draw.ellipse(surf, yellow, (sx - 5, flame_y - 32, 10, 20))
            pygame.draw.ellipse(surf, white, (sx -2, flame_y - 40, 5,20))


        def hits(self, prect, cam):
            sx = self.wx - cam

            return pygame.Rect(sx-7, Ground - self.h - 8, 14, self.h + 8).colliderect(prect)