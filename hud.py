import pygame


def draw_hud(surf, lives, ques_done, ques_total, distance):
    hud_font = pygame.font.SysFont("Arial", 18, bold=True)

    for i in range(3):
        heart_color = pygame.Color("red")

        hx = 20 + i*32
        hy = 16

        pygame.draw.circle(surf, heart_color, (hx + 6, hy + 6), 6)
        pygame.draw.circle(surf, heart_color, (hx + 16, hy + 6), 6)

        triangle_points = [(hx, hy + 9), (hx + 22, hy + 9), (hx + 11, hy + 20)]
        pygame.draw.polygon(surf, heart_color, triangle_points)


    bar_x = (W//2) - 130
    bar_y = 10
    bar_w = 260
    bar_h = 22

    pygame.draw.rect(surf, dkgray, (bar_x, bar_y, bar_w, bar_h))

    if ques_total > 0:
        percentage = ques_done/ques_total
        width = int(bar_w * percentage)

        if width > 0:
            pygame.draw.rect(surf, purple, (bar_x, bar_y, width, bar_h))

    pygame.draw.rect(surf, white, (bar_x, bar_y, bar_w, bar_h), 2)


    quiz_str = f"Quiz: {ques_done} / {ques_total}"
    quiz_txt_img = hud_font.render(quiz_str, True, White)

    text_x = (W // 2) - (quiz_txt_img.get_width() // 2)
    surf.blit(quiz_txt_img, (text_x, bar_y + 2))

    distance_str = f"Dist: {distance}"
    distance_txt_img = hud_font.render(distance_str, True, white)
    surf.blit(distance_txt_img, (W - 120, bar_y + 2))