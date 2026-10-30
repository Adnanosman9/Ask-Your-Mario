import pygame
import random

trunk = pygame.Color("brown1")
leaf_1 = pygame.Color("green2")

class Background:
    def __init__(self, world_L):
        rng = random.Random(42)

        self.bg_trees = []
        for _ in range(40):
            tree_x = rng.randint(0, world_L)
            tree_y = rng.randint(220, 320)
            scale = rng.uniform(0.7, 1.0)
            self.bg_trees.append((tree_x, tree_y, scale))


        self.fg_trees = []
        for _ in range(30):
            tree_x = rng.randint(0, world_L)
            scale = rng.uniform(1.1, 1.4)
            self.fg_trees.append((tree_x, scale))

        self.clouds = []
        for _ in range(20):
            cloud_x = rng.randint(0, world_L)
            cloud_y = rng.randint(35, 120)
            self.clouds.append((cloud_x, cloud_y))

        self.vines = []
        for _ in range(15):
            vine_x = rng.randint(0, world_L)
            vine_y = rng.randint(50, 120)
            self.vines.append((vine_x, vine_y))


    def tree(self, surf, x, y, scale, dark):
        body = trunk
        leaf = leaf_1

        body_w = int(14 * scale)
        body_h = int(55 * scale)
        pygame.draw.rect(surf, body, (x - body_w // 2, y, body_w, body_h))

        pygame.draw.circle(surf, leaf, (x,y), int(35 * scale))
        pygame.draw.circle(surf, leaf, (x,y - int(18 * scale)), int(28 * scale))
        pygame.draw.circle(surf, leaf, (x,y - int(34 * scale)), int(20 * scale))


    def cloude(self, surf, x,y):
        cloud_color = pygame.Color("peachpuff3")

        pygame.draw.circle(surf, cloud_color, (x -20, y), 20)
        pygame.draw.circle(surf, cloud_color, (x+20, y), 20)
        pygame.draw.circle(surf, cloud_color, (x, y-8), 25)
        pygame.draw.circle(surf, cloud_color, (x, y+4), 22)


    def vine(self, surf, x, L):
        pygame.draw.line(surf, leaf_2, (x,0), (x, L), 3)

        seg = L // 20
        for i in range(seg):
            leaf_y = i * 20 + 10
            pygame.draw.circle(surf, leaf_1, (s + 4, leaf_y), 4)


    def sky_layer(self, surf, cam):
        surf.fill(sky, (0, 0, W, Ground))

        for cx, cy in self.clouds:
            sx = int(cx - (cam * 0.1))
            if -50 < sx < W + 50:
                self.cloude(surf, sx, cy)

        for tx, ty, scale in self.bg_trees:
            sx = int(tx - (cam * 0.4))
            if -50 < sx < W + 50:
                self.tree(surf, sx, ty, scale, dark=True)


        for vx, vlen in self.vines:
            sx = int(vx - (cam * 0.6))
            if -20 < sx < W+20:
                self.vine(surf, sx, vlenf)


    def ground_layer(self, surf, cam):
        pygame.draw.rect(surf, grass, (0, Ground, W, 24))

        pygame.draw.rect(surf, dirt, (0, Ground + 24, W, H-Ground - 24))

        for tx, scale in self.fg_trees:
            sx = int(tx - cam)
            base_y = Ground - int(50 * scale)

            if - 60 < sx < W+ 60:
                self.tree(surf, sx, base_y, scale, dark=False)