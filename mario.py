import pygame
import sys
import random


pygame.init()

W, H = 900, 520
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Sky")
clock = pygame.time.Clock()
FPS = 60


Ground = 390
Player_x = 135
Length = 12000

# sky     = pygame.Color("skyblue")
# leaf_1  = pygame.Color("green2")
# leaf_2  = pygame.Color("darkgreen")
# trunk   = pygame.Color("brown1")
# Grass   = pygame.Color("Green")
# dirt    = pygame.Color("brown")
# white   = pygame.Color("white")
# red     = pygame.Color("red")
# orange  = pygame.Color("orange")
# yellow  = pygame.Color("yellow")
# gold    = pygame.Color("yellow3")
# purple  = pygame.Color("purple3")
# gray    = pygame.Color("grey")
# dkgray  = pygame.Color("grey4")
# skin    = pygame.Color("peachpuff1")
# brown   = pygame.Color("brown")
# LTpurp  = pygame.Color("purple")
# crimson = pygame.Color("crimson")

black   = pygame.Color("black")

Quiz = [
    {"q": "..............?", "a": "......"},
    {"q": "..............?", "a": "......"},
    {"q": "..............?", "a": "......"},
    {"q": "..............?", "a": "......"},
    {"q": "..............?", "a": "......"},
]


def center_text(surface, text, font, color, center_x, center_y, shadow=False):
    if shadow:
        shadow_img = font.render(text, True, black)
        shadow_rect = shadow_img.get_rect(center=(center_x + 2, center_y + 2))
        surface.blit(shadow_img, shadow_rect)
        
    text_img = font.render(text, True, color)
    text_rect = text_img.get_rect(center=(center_x, center_y))
    surface.blit(text_img, text_rect)


from player import Player
from background import Background
from spikes import Spikes
from firepiller import firepillar
from sage import Sage
from dialogue import Dialogue
from hud import draw_hud
from warning import draw_warning
from particle import hit_particles
from over import over_screen
from win_screen import win_screen
from tittle import title_screen



def build_world():
    sages = []
    obstacles = []
    

    sage_x = 1800

    for question in Quiz:
        sages.append(Sage(sage_x))


        obstacles.append(Spikes(sage_x - 800))
        obstacles.append(Spikes(sage_x - 500))


        obstacles.append(firepillar(sage_x - 250))


        sage_x += 1800

    return sages, obstacles



def run_game():
    total_questions = len(Quiz)
    title_screen(screen, total_questions)


    player = Player()
    background = Background(Length)
    sages, obstacles = build_world()


    camera_x = 0
    scroll_speed = 3
    current_question = 0
    active_dialog = None
    particles = []

    while True:
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if active_dialog:
                active_dialog.handle(event)
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
                        player.jump()


        if active_dialog:
            active_dialog.update()

            if active_dialog.finished():
                if active_dialog.status == "correct":
                    sages[current_question].active = False
                    current_question += 1


                    if current_question >= total_questions:
                        distance = camera_x // 100
                        win_screen(screen, distance)
                        return

                    active_dialog = None
                    scroll_speed = 3
                else:
                    over_screen(screen, "Wrong answer!")
                    return

        else:
            
            camera_x += scroll_speed
            if camera_x > Length - W:
                camera_x = Length - W

            player.update()


            if player.invincible_frames == 0:
                for obstacle in obstacles:
                    if obstacle.hits(player.rect, camera_x):
                        player.lives -= 1
                        player.invincible_frames = 90
                        
                        new_particles = hit_particles(player.x + 15, player.y + 24)
                        particles.extend(new_particles)

                        if player.lives <= 0:
                            over_screen(screen, "You were hit!")
                            return
                        break


            if current_question < total_questions:
                sage = sages[current_question]
                if sage.active:
                    sage_screen_x = sage.wx - camera_x

                    
                    if sage_screen_x > Player_x - 60 and sage_screen_x < Player_x + 60:
                        scroll_speed = 0
                        question_data = Quiz[current_question]
                        active_dialog = Dialogue(question_data, current_question + 1, total_questions)


        alive_particles = []
        for particle in particles:
            particle.update()
            if particle.current_life > 0:
                alive_particles.append(particle)
        particles = alive_particles


        background.sky_layer(screen, camera_x)
        background.ground_layer(screen, camera_x)

        for obstacle in obstacles:
            obstacle.draw(screen, camera_x)

        for sage in sages:
            sage.draw(screen, camera_x)

        player.draw(screen)

        for particle in particles:
            particle.draw(screen)


        if not active_dialog:
            draw_warning(screen, obstacles, camera_x)

        distance_meters = camera_x // 100
        draw_hud(screen, player.lives, current_question, total_questions, distance_meters)


        if active_dialog:
            active_dialog.draw(screen)

        pygame.display.flip()



while True:
    run_game()
