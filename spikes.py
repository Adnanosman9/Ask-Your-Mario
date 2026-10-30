import pygame
import random

# Ground = 390
# gray = pygame.Color("grey")

# W, H = 900, 520


class Spikes:
    def __init__(self, wx):
        self.wx = wx
        self.n = random.randint(2, 5) 
        self.w = self.n * 20          

    def draw(self, surf, cam):
        sx = self.wx - cam
        
        if not (-self.w - 20 < sx < W + 20):
            return

        for i in range(self.n):
            spike_x = sx + (i * 20)
            
            points = [
                (spike_x, Ground),           
                (spike_x + 10, Ground - 26),  
                (spike_x + 20, Ground)        
            ]
            
            pygame.draw.polygon(surf, (70, 70, 70), points)
            pygame.draw.polygon(surf, gray, points, 1)

    def hits(self, prect, cam):
        sx = self.wx - cam
        
        hitbox = pygame.Rect(sx + 4, Ground - 22, self.w - 8, 22)
        
        return hitbox.colliderect(prect)