import pygame
import sys
from mario import Quiz

W, H = 900, 520
screen = pygame.display.set_mode((W, H))
Ground = 390

sky = pygame.Color("skyblue")
leaf_1 = pygame.Color("green2")
leaf_2 = pygame.Color("darkgreen")
trunk = pygame.Color("brown1")
Grass = pygame.Color("Green")
dirt = pygame.Color("brown")
white = pygame.Color("white")
red = pygame.Color("red")
yellow = pygame.Color("yellow")
gold = pygame.Color("yellow3")
purple = pygame.Color("purple3")
skin = pygame.Color("peachpuff1")

def title_screen():
    tittle_font = pygame.font.Font("Arial", 42, bold=True)
    subtitle_font = pygame.font.Font("Arial", 24, bold=True)
    menu_font = pygame.font.Font("Arial", 18, bold=True)

    tree_wave = 0
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                return

        screen.fill(sky, (0, 0, W, Ground))

        pygame.draw.rect(screen, Grass, (0, Ground, W, 24))
        pygame.draw.rect(screen, dirt, (0, Ground + 24, W, 24))

        tree_wave += 1
        for i in range(7):
            tx = 60 + (i *135) 

            if (tree_wave // 15) % 2 == 0:
                scale = 1.05 if i % 2 == 0 else 0.95
            else:
                scale = 0.95 if i % 2 == 0 else 1.05

            pygame.draw.rect(screen, trunk, (tx - 9, Ground - 62, 18, 62))
            pygame.draw.circle(screen, leaf_1, (tx, Ground - 62), int(30 * scale))
            pygame.draw.circle(screen, leaf_2, (tx, Ground - 78), int(25 * scale))
            pygame.draw.circle(screen, pygame.Color("Green3"), (tx, Ground - 62), int(20 * scale))


        wx2, wy2 = 60, 310
        pygame.draw.circle(screen, skin, (wx2, wy2), 20)
        pygame.draw.polygon(screen, purple, [(wx2 - 20, wy2 - 2), (wx2 + 20, wy2 - 2), (wx2, wy2 + 40)])
        pygame.draw.rect(screen, purple, (wx2 - 20, wy2 - 5, 40, 10), border_radius=5)
        pygame.draw.circle(screen, yellow, (wx2, wy2-36), 8)
        pygame.draw.ellipse(screen, white, (wx2 - 10, wy2 + 10, 20, 10))

        qs_text = tittle_font.render("?", True, gold)
        screen.blit(qs_text, (wx2+20, wy2-40))


        pygame.draw.rect(screen, pygame.Color("Navy"), (W // 2 - 320, 90, 640, 100))
        pygame.draw.rect(screen, purple, (W // 2 - 320, 90, 640, 100), 2, border_radius=10)


        heading = tittle_font.render("Welcome..........", True, gold)
        screen.blit(heading, (W // 2 - heading.get_width() // 2, 100))

        subheading = subtitle_font.render("Press any key to start", True, white)
        screen.blit(subheading, (W // 2 - subheading.get_width() // 2, 150))


        pygame.draw.rect(screen, pygame.Color("Navy"), (W // 2 - 280, 212, 560, 132))
        pygame.draw.rect(screen, purple, (W // 2 - 280, 212, 560, 132), 2, border_radius=10)


        line1 = menu_font.render("Use Space to Jump", True, white)
        screen.blit(line1, (W // 2 - line1.get_width() // 2, 220))


        line2 = menu_font.render("reach the wizard for his questions", True, yellow)
        screen.blit(line2, (W // 2 - line2.get_width() // 2, 250))

        line3 = menu_font.render("Wrong ans = Game over!", True, red)
        screen.blit(line3, (W // 2 - line3.get_width() // 2, 280))

        quiz_length = len(Quiz) if 'Quiz' in globals() else 5
        line4 = menu_font.render(f"Clear all Questions: {quiz_length}", True, white)
        screen.blit(line4, (W // 2 - line4.get_width() // 2, 310))


        current_tick = pygame.time.get_ticks()
        if (current_tick // 540) % 2 == 0:
            starter_text = menu_font.render("Press any key to start", True, white)
            screen.blit(starter_text, (W // 2 - starter_text.get_width() // 2, 340))


        pygame.display.flip()