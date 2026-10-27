import pygame

pygame.init()

colors = [
    pygame.Color("crimson"),
    pygame.Color("peachpuff1"),
    pygame.Color("peachpuff2"),
    pygame.Color("peachpuff3"),
    pygame.Color("peachpuff4")
]

count = len(colors)
cols = 3
rows = (count + cols - 1) // cols

w = 270 * cols
h = 160 * rows

print(len(colors))
print(w)
print(h)

screen = pygame.display.set_mode((w,h))
font = pygame.font.SysFont("Arial", 16)


running = True

while running:
    screen.fill((30,30,30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    for i, color in enumerate(colors):
        row = i // cols
        col = i % cols

        x = col * 270
        y = row * 160

        rect = pygame.Rect(x,y, 270, 160)

        pygame.draw.rect(screen, color, rect, border_radius=8)
        pygame.draw.rect(screen, pygame.Color('grey4'), rect, width=2, border_radius=8)

        name = font.render(f"Color {i+1}", True, pygame.Color("black"))
        rgb = font.render(f"RGB: ({color.r}, {color.g}, {color.b})", True, pygame.Color("red"))
        hex = font.render(f"Hex: #{color.r:02x}{color.g:02x}{color.b:02x}".upper(), True, pygame.Color("green"))


        cx = x + 270 // 2
        # screen.blit(name, (cx - name))
        screen.blit(name, (cx - name.get_width() // 2, y + 35))
        screen.blit(rgb,  (cx - rgb.get_width() // 2,  y + 70))
        screen.blit(hex,  (cx - hex.get_width() // 2,  y + 100))

    pygame.display.flip()

pygame.quit()