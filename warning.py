import pygame
import sys

pygame.init()

def draw_warning(surf, obstacles, cam):
    warn_font = pygame.font.SysFont("Arial", 22, bold=True)
    dist_font = pygame.font.SysFont("Arial", 12, bold=True)

    closest_x = None

    for obs in obstacles:
        screen_x = obs.wx - cam

        if 280 < screen_x < 520:
            if closest_x is None or screen_x < closest_x:
                closest_x = screen_x

    if closest_x is None:
        return


    current_time = pygame.time.get_ticks()
    if(current_time // 200) % 2 == 0:
        color = red 
        text_color = white

    else:
        color = orange 
        txt_color = black


    alert_x = W - 75
    alert_y = Ground - 75


    arrow_points = [
        (alert_x, alert_y + 15),
        (alert_x + 18, alert_y + 2),
        (alert_x + 18, alert_y + 28)
    ]

    pygame.draw.polygon(surf, color, arrow_points)
    pygame.draw.rect(surf, color, (alert_x + 18, alert_y+ 8, 22, 14))

    badge = (alert_x + 48, alert_y + 15)

    pygame.draw.circle(surf,color, badge, 15)
    pygame.draw.circle(surf, black, badge, 15,2)

    exclamation = warn_font.render("!", True, text_color)
    text_x = badge[0] - (exclamation.get_width()/ 2)
    text_y = badge[1] - (exclamation.get_width()/ 2)

    surf.blit(exclamation, (text_x, text_y))

    distance_rem = int(closest_x - Player)

    if distance_rem > 0:
        distance_str = f"{distance_rem}px"
        distance_img = dist_font.render(distance_str, True, orange)

        dist_x = (alert_x + 25) - (distance_img.get_width() // 2)
        surf.blit(distance_img, (dist_x, alert_y + 35))