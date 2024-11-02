import pygame

class Room1:
    def __init__(self, screen, s_width, s_height) -> None:
        self.screen = screen
        self.s_w, self.s_h = s_width, s_height

        self.font = pygame.font.SysFont("Arial", 50)

        self.entrance_text = self.font.render("ENTRANCE", True, 'black')
        self.entrance_rect = self.entrance_text.get_rect()
        self.entrance_rect.center = (s_width/2, 15)

        

        # self.w = width
        # self.h = height

    def draw(self):
        pygame.draw.rect(self.screen, 'black', )

    def update(self):
        self.draw()