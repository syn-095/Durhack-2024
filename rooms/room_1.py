import pygame

class Room1:
    def __init__(self, screen, s_width, s_height) -> None:
        self.screen = screen
        self.s_w, self.s_h = s_width, s_height

        self.font = pygame.font.SysFont("Arial", 50)

        self.entrance_text = self.font.render("ENTRANCE", True, 'black')
        self.entrance_rect = self.entrance_text.get_rect()
        self.entrance_rect.midtop = (s_width/2, 15)

        self.nxt_room_txt = self.font.render("NEXT ROOM", True, 'black')
        self.nxt_room_rect = self.nxt_room_txt.get_rect()
        self.nxt_room_rect.midbottom = (s_width/2, self.s_h/2)

        self.hover_rect = pygame.Rect(0,0,self.nxt_room_rect.width + 5, self.nxt_room_rect.height + 5)
        self.hover_rect.center = self.nxt_room_rect.center

    def hover_effect(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        if self.nxt_room_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, 'grey', self.hover_rect, 0, 2)
            if click: return True

    def draw(self):
        self.screen.blit(self.entrance_text, self.entrance_rect)
        self.screen.blit(self.nxt_room_txt, self.nxt_room_rect)

    def update(self):
        exit=self.hover_effect()
        self.draw()

        return exit

class Room2:
    def __init__(self, screen, s_width, s_height) -> None:
        self.screen = screen
        self.s_w, self.s_h = s_width, s_height

        self.font = pygame.font.SysFont("Arial", 50)

        self.room_number_text = self.font.render("001", True, 'black')
        self.room_number_rect = self.room_number_text.get_rect()
        self.room_number_rect.midtop = (s_width/2, 15)

        self.nxt_room_txt = self.font.render("NEXT ROOM", True, 'black')
        self.nxt_room_rect = self.nxt_room_txt.get_rect()
        self.nxt_room_rect.midbottom = (s_width/2, self.s_h/2)

        self.back_txt = self.font.render("BACK", True, 'black')
        self.back_rect = self.back_txt.get_rect()
        self.back_rect.midbottom = (s_width/2, self.s_h/2 + 60)  # Adjust as necessary

        self.hover_rect_next = pygame.Rect(0, 0, self.nxt_room_rect.width + 5, self.nxt_room_rect.height + 5)
        self.hover_rect_next.center = self.nxt_room_rect.center

        self.hover_rect_back = pygame.Rect(0, 0, self.back_rect.width + 5, self.back_rect.height + 5)
        self.hover_rect_back.center = self.back_rect.center

    def hover_effect(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.nxt_room_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, 'grey', self.hover_rect_next, 0, 2)

        if self.back_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, 'grey', self.hover_rect_back, 0, 2)

    def draw(self):
        self.screen.blit(self.room_number_text, self.room_number_rect)
        self.screen.blit(self.nxt_room_txt, self.nxt_room_rect)
        self.screen.blit(self.back_txt, self.back_rect)

    def update(self):
        self.hover_effect()
        self.draw()