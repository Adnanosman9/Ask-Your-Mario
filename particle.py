import pygame
import random

# red = pygame.Color("red")
# orange = pygame.Color("orange")
# yellow = pygame.Color("yellow")
# gold = pygame.Color("yellow3")
# purple = pygame.Color("purple3")

class Particle:
    def __init__(self, x, y, color, speed_x, speed_y):
        self.x = float(x)
        self.y = float(y)
        self.vx = speed_x
        self.vy = speed_y
        self.color = color

        self.max_life = random.randint(20, 40)
        self.current_life = self.max_life


    def update(self):
        self.x += self.vx
        self.y += self.vy

        self.vy += 0.3

        self.current_life -= 1

    def draw(self, surf):
        life_ratio = self.current_life / self.max_life
        radius = int(5 * life_ratio)

        if radius > 0 and self.current_life > 0:
            pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), radius)


def hit_particles(x,y):

    colors = [red, orange, yellow]
    particle_list = []

    for _ in range(18):
        random_vx = random.uniform(-4, 4)
        random_vy = random.uniform(-6, -1)

        new_particle = Particle(x, y, random.choice(colors), random_vx, random_vy)
        particle_list.append(new_particle)

    return particle_list


def confetti(amount = 60):
    colors = [gold, yellow, purple, red, orange]
    confetti_list = []

    for _ in range(amount):
        spawn_x = random.randint(0, W)
        spawn_y = random.randint(-20, 0)

        random_vx = random.uniform(-2, 2)
        random_vy = random.uniform(2, 6)

        new_particle =  Particle(spawn_x, spawn_y, random.choice(colors), random_vx, random_vy)
        confetti_list.append(new_particle)

    return confetti_list

    