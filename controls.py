import pygame
import sys

pygame.init()

W, H = 900, 520

purple = pygame.Color("purple3")
LTpurp = pygame.Color("purple")
screen = pygame.display.set_mode((W, H))
blue = pygame.Color("blue")
white = pygame.Color("white")

def draw_controls(surf):

    control_font = pygame.font.SysFont("Arial", 12, bold=True)

    box_w, box_h = 188, 68
    box_x = 10
    box_y = H - box_h -10

    pygame.draw.rect(surf, pygame.Color("blue4"), (box_x, box_y, box_w, box_h))
    pygame.draw.rect(surf, purple, (box_x, box_y, box_w, box_h), 2)

    title_img = control_font.render("Controls", True, LTpurp)
    title_x = box_x + (box_w // 2) - (title_img.get_width() // 2)
    surf.blit(title_img, (title_x, box_y + 6))

    pygame.draw.line(surf, purple, (box_x + 8, box_y + 22), (box_x + box_w - 8, box_y + 22), 1)

    space_box_x = box_x + 8
    space_box_y = box_y + 28

    space_box_w, space_box_h = 52, 14

    pygame.draw.rect(surf, purple, (space_box_x, space_box_y, space_box_w, space_box_h))
    pygame.draw.rect(surf, blue, (space_box_x, space_box_y, space_box_w, space_box_h), 1)

    space_label = control_font.render("Space", True, blue)
    surf.blit(space_label, (space_box_x + 5, space_box_y + 1))

    up_box_x = box_x + 8
    up_box_y = box_y + 46
    up_box_w, up_box_h = 52, 14

    pygame.draw.rect(surf, purple, (up_box_x, up_box_y, up_box_w, up_box_h))
    pygame.draw.rect(surf, blue, (up_box_x, up_box_y, up_box_w, up_box_h), 1)

    up_label = control_font.render("Up / W", True, blue)
    surf.blit(up_label, (up_box_x + 5, up_box_y + 1))

    jump_label = control_font.render("jump", True, white)
    surf.blit(jump_label, (up_box_x + up_box_w + 6, up_box_y + 1))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((40, 40, 40))

    draw_controls(screen)

    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
sys.exit()