import sys
import pygame

# W, H = 900, 520
# screen = pygame.display.set_mode((W, H))

# gray = pygame.Color("grey")
# dkgray = pygame.Color("grey4")
# white = pygame.Color("white")
# red = pygame.Color("red")


def over_screen(reason):
    clock = pygame.time.Clock()
    over_font = pygame.font.SysFont("Arial", 46, bold=True)
    reason_font = pygame.font.SysFont("Arial", 24, bold=True)

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                return


        screen.fill((40, 0, 0))

        skull_x = W // 2
        skull_y = 110


        pygame.draw.circle(screen, gray, (skull_x, skull_y), 45)
        pygame.draw.rect(screen, gray, (skull_x - 20, skull_y + 28, 40, 16), border_radius=4)

        pygame.draw.circle(screen, dkgray, (skull_x - 15, skull_y - 10), 8)
        pygame.draw.circle(screen, dkgray, (skull_x + 15, skull_y - 10), 8)

        for i in range(4):
            teeth_x = skull_x - 16 + i * 10
            pygame.draw.rect(screen, dkgray, (teeth_x, skull_y + 28, 4, 16))


        tittle_text = over_font.render("Game Over", True, red)
        tittle_x = W // 2 - tittle_text.get_width() // 2
        screen.blit(tittle_text, (tittle_x, 195))

        reason_text = reason_font.render(reason, True, white)
        reason_x = W // 2 - reason_text.get_width() // 2
        screen.blit(reason_text, (reason_x, 265))

        pygame.display.flip()