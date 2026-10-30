import pygame 

purple = pygame.Color("purple3")
Ground = 390
W, H = 900, 520

F_LG = pygame.font.SysFont("Arial", 28, Bold= True)

class Sage:
    def __init__(self, wx):
        self.wx = wx
        self.active = True
        self.frame = 0

        self.bob_y = 0
        self.question_y = 0
        self.spark_x = 0
        self.spark_y = 0

    def screen_x(self, cam):
        return self.wx - cam

    def draw(self, surf, cam):
        if not self.active:
            return

        self.frame += 1
        sx = self.wx - cam

        if not (-80 < sx < W+80):
            return

        if self.frame % 8 == 0:

            seq = [0,2,4,2,0,-2,-4,-2]
            self.bob_y = seq[(self.frame // 8) % len(seq)]

        if self.frame % 6 == 0:
            qsec = [0,3,6,3,0,-3,-6,-3]
            self.question_y = qsec[(self.frame // 6) % len(qsec)]


        spark = [
            (10,0), (7,7), (0,10), (-7,7),
            (-10,0), (-7,-7), (0,-10), (7,-7)
        ]
        self.spark_x, self.spark_y = spark[(self.frame // 4) % len(spark)]


        px = int(sx)
        py = int(Ground - 60 + self.bob_y)


        robe_points = [
            (px + 2, py+ 20),
            (px + 36, py+ 20),
            (px+42, Ground)
            (px - 4, Ground)
        ]

        pygame.draw.polygon(surf, purple, robe_points)
        pygame.draw.polygon(surf, LTpurp, robe_points, 2)

        pygame.draw.circle(surf, yellow, (px+10, py+35,), 2)
        pygame.draw.circle(surf, yellow, (px+28, py+45), 2)
        pygame.draw.circle(surf, yellow, (px+18, py+55), 2)

        pygame.draw.circle(surf, skin, (px+19, py+12), 13)
        pygame.draw.ellipse(surf, white, (px+8, py+20, 22,12))
        pygame.draw.ellipse(surf, gray, (px+10, p+21, 18, 9))


        # pygame.draw.polygon(surf, purple, (px + 5, py + 4), (px + 33, py + 4), (px + 19, py - 28))

        hat = [(px + 5, py + 4), (px + 33, py + 4), (px + 19, py - 28)]
        pygame.draw.polygon(surf, purple, hat)
        pygame.draw.polygon(surf, LTpurp, hat, 2)
        pygame.draw.rect(surf, purple, (px+2, py+1, 34, 9), border_radius=4)


        pygame.draw.circle(surf, yellow, (px+19, py-28,), 5)
        pygame.draw.circle(surf, white, (px+19, py-28), 3)

        pygame.draw.circle(surf, white, (px+13, py+12,), 4)
        pygame.draw.circle(surf, purple, (px+13, py+12), 2)
        pygame.draw.circle(surf, (px+14, py+11), 1)

        pygame.draw.circle(surf, white, (px+25, py+12), 4)
        pygame.draw.circle(surf, purple, (px+25, py+12), 2)
        pygame.draw.circle(surf, white, (px+26, py+11), 1)


        pygame.draw.rect(surf, brown, (px+40, py-8, 5, 48))
        pygame.draw.circle(surf, gold, (px+42, py-8), 8)
        pygame.draw.circle(surf, yellow, (px+42, py-8), 5)


        pygame.draw.circle(surf, white, (px+42 + self.spark_x, py - 8+ self.spark_y), 3)

        ques = F_LG.render("?", True, gold)

        surf.blit(ques, (px+8, py-56 + self.question_y))