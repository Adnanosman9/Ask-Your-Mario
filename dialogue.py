import pygame

white = pygame.Color("white")
yellow = pygame.Color("yellow")


class Dialogue:
    def __init__(self, ques_data, ques_number, total_ques):

        self.question = ques_data["q"]
        self.answer = ques_data["a"].strip().lower()

        self.num = ques_number
        self.total = total_ques
        self.typed = ""
        self.status = "typing"
        self.timer = 0

    def handle(self, event):

        if self.status != "typing":
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                player_guess = self.typed.strip().lower()

                if player_guess == self.answer:
                    self.status = "correct"
                    self.timer = 90

                else:
                    self.status = "wrong"
                    self.timer = 120

            elif event.key == pygame.K_BACKSPACE:
                self.typed = self.typed[:-1]

            elif len(self.typed) < 25:
                if event.unicode.isprintable():
                    self.typed += event.unicode


    def update(self):

        if self.timer > 0:
            self.timer -= 1

    def finished(self):

        return self.status != "typing" and self.timer == 0


    def draw(self, surf):
        quiz_font = pygame.font.SysFont("Arial", 24)

        overlay = pygame.Surface(((900, 520)))
        overlay.fill((30,30,30))
        overlay.set_alpha(200)
        surf.blit(overlay, (0,0))


        box_x, box_y = 150, 100
        box_w, box_h = 600, 320

        pygame.draw.rect(surf, pygame.Color("red"), (box_x, box_y, box_w, box_h))
        pygame.draw.rect(surf, pygame.Color("purple"), (box_x, box_y, box_w, box_h), 4)

        tittle_img = quiz_font.render(f"Question {self.num} of {self.total}", True, pygame.Color("yellow"))

        surf.blit(tittle_img, (box_x + 40, box_y+ 20))

        wrapped_lines = wordss(self.question, quiz_font, max_w = 520)
        for i, line in enumerate(wrapped_lines):
            line_img = quiz_font.render(line, True, pygame.Color("white"))
            surf.blit(line_img, (box_x + 40, box_y + 70 + (i * 30)))


        input_rect = pygame.Rect(box_x + 40, box_y + 180, 520, 45)
        pygame.draw.rect(surf, white, input_rect)
        pygame.draw.rect(surf, pygame.Color("purple3"), input_rect, 2)


        text_img = quiz_font.render(self.typed, True, pygame.Color("black"))
        surf.blit(text_img, (input_rect.x + 10, input_rect.y + 10))

        if self.status == "correct":
            msg = quiz_font.render("Correct", True, pygame.Color("green"))
            surf.blit(msg, (box_x + 40, box_y + 250))

        elif self.status == "wrong":
            msg = quiz_font.render(f"Wrong, Answer: {self.answer}", True, pygame.Color("red"))
            surf.blit(msg, box_x+40, box_y + 250)

        else:
            msg = quiz_font.render("Press Enter", True, yellow)
            surf.blit(msg, (box_x + 40, box_y + 250))
