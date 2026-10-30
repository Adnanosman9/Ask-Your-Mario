import pygame


# Ground = 390
# player = 135

# brown = pygame.Color("brown")
# skin = pygame.Color("peachpuff1")
# black = pygame.Color("black")

class Player:
    width, height = 30, 48

    def __init__(self):
        
        self.x = float(player)  
        self.y = float(Ground)
        self.velocity_y = 0.0
        self.on_ground = True

        
        self.lives = 3
        self.frame = 0
        self.invincible_frames = 0
        self.animation_state = "walk_left_foot"  
    def jump(self):
        if self.on_ground:
            self.velocity_y = -17.0
            self.on_ground = False

    def update(self):
        
        self.velocity_y += 0.5
        self.y += self.velocity_y
        
        floor_level = float(Ground - self.height)
        if self.y >= floor_level:
            self.y = floor_level
            self.velocity_y = 0.0
            self.on_ground = True
        else:
            self.on_ground = False


        self.frame += 1

        
        if self.on_ground and self.frame % 6 == 0:
            if self.animation_state == "walk_left_foot":
                self.animation_state = "walk_right_foot"
            else:
                self.animation_state = "walk_left_foot"


        if self.invincible_frames > 0:
            self.invincible_frames -= 1

    @property
    def rect(self):
        
        return pygame.Rect(int(self.x) + 4, int(self.y) + 4, self.width - 8, self.height - 4)

    def draw(self, surf):
        
        if self.invincible_frames > 0 and (self.frame % 6 < 3):
            return

        px, py = int(self.x), int(self.y)


        if not self.on_ground:
            left_leg_h, right_leg_h = 10, 10
            left_arm_y, right_arm_y = py + 20, py + 20
        elif self.animation_state == "walk_left_foot":
            left_leg_h, right_leg_h = 13, 7
            left_arm_y, right_arm_y = py + 25, py + 15
        else:
            left_leg_h, right_leg_h = 7, 13
            left_arm_y, right_arm_y = py + 15, py + 25


        pygame.draw.rect(surf, brown, (px + 6, py + 37, 8, left_leg_h), border_radius=3)   
        pygame.draw.rect(surf, brown, (px + 16, py + 37, 8, right_leg_h), border_radius=3)
        pygame.draw.rect(surf, skin, (px - 4, left_arm_y, 9, 6), border_radius=3)       
        pygame.draw.rect(surf, skin, (px + 25, right_arm_y, 9, 6), border_radius=3)       


        pygame.draw.rect(surf, (55, 160, 55), (px + 5, py + 18, 20, 20), border_radius=3)  
        pygame.draw.rect(surf, brown, (px + 5, py + 33, 20, 4))                          


        pygame.draw.circle(surf, skin, (px + 15, py + 11), 11)     
        pygame.draw.circle(surf, black, (px + 11, py + 11), 2)     
        pygame.draw.circle(surf, black, (px + 19, py + 11), 2)      
        pygame.draw.arc(surf, black, (px + 9, py + 13, 12, 6), 3.14, 6.28, 2) 

        pygame.draw.rect(surf, brown, (px + 5, py - 5, 20, 10), border_radius=3)
        pygame.draw.rect(surf, brown, (px + 1, py + 1, 28, 6), border_radius=2)
        pygame.draw.rect(surf, (80, 40, 10), (px + 5, py + 1, 20, 3))
