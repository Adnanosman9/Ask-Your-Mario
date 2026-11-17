import pygame
import sys

from particle import confetti


W = 900
H = 520
C = 450

white = pygame.Color("white")
gray = pygame.Color("grey")
gold = pygame.Color("yellow3")
black = pygame.Color("black")
green = pygame.Color("green4")


def win_screen(screen, distance):
    clock = pygame.time.Clock()
    tittle_font = pygame.font.SysFont("Arial", 36, bold=True)
    text_font = pygame.font.SysFont("Arial", 22, bold=False)


    confetti_list = confetti(60)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return


        screen.fill(green)


        for piece in confetti_list:
            piece.update()
            piece.draw(screen)


        alive_confetti = []
        for piece in confetti_list:
            if piece.current_life > 0:
                alive_confetti.append(piece)
        confetti_list = alive_confetti


        if len(confetti_list) < 80:
            new_pieces = confetti(10)
            confetti_list.extend(new_pieces)


        shadow_text = tittle_font.render("You Win!", True, black)
        shadow_box = shadow_text.get_rect(center=(452, 152))
        screen.blit(shadow_text, shadow_box)

        title_text = tittle_font.render("You Win!", True, gold)
        title_box = title_text.get_rect(center=(C, 150))
        screen.blit(title_text, title_box)


        messages = [
            ("You answered all questions correctly!", white),
            (f"Distance covered: {distance}m", gray),
            ("Press any key to play again", gray),
        ]

        text_y = 230
        for line, color in messages:
            line_text = text_font.render(line, True, color)
            line_box = line_text.get_rect(center=(C, text_y))
            screen.blit(line_text, line_box)
            text_y += 50


        pygame.display.flip()
        clock.tick(60)
