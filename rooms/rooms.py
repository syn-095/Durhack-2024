import pygame, time

class DefaultRoom:
    def __init__(self, screen, s_width, s_height, room_name : str, no_room_display = False, no_room_back = False):
        self.screen = screen
        self.s_w, self.s_h = s_width, s_height

        self.font = pygame.font.SysFont("Arial", 50)

        if not no_room_display:
            self.room_number_text = self.font.render(f"{room_name}", True, 'black')
            self.room_number_rect = self.room_number_text.get_rect()
            self.room_number_rect.midtop = (s_width/2, 15)

        if not no_room_back:
            self.back_txt = self.font.render("BACK", True, 'black')
            self.back_rect = self.back_txt.get_rect()
            self.back_rect.midbottom = (s_width/2, s_height - 60)

class Entrance(DefaultRoom):
    def __init__(self, screen, s_width, s_height) -> None:
        super().__init__(screen, s_width, s_height, "ENTRANCE")

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
            if click: 
                return "next"

    def draw(self):
        self.screen.blit(self.room_number_text, self.room_number_rect)
        self.screen.blit(self.nxt_room_txt, self.nxt_room_rect)

    def update(self):
        exit=self.hover_effect()
        self.draw()

        return exit

class Room1(Entrance):
    def __init__(self, screen, s_width, s_height) -> None:
        super().__init__(screen, s_width, s_height)

        self.room_number_text = self.font.render("001", True, 'black')
        self.room_number_rect = self.room_number_text.get_rect()
        self.room_number_rect.midtop = (s_width/2, 15)

        self.hover_rect_next = pygame.Rect(0, 0, self.nxt_room_rect.width + 5, self.nxt_room_rect.height + 5)
        self.hover_rect_next.center = self.nxt_room_rect.center

        self.hover_rect_back = pygame.Rect(0, 0, self.back_rect.width + 5, self.back_rect.height + 5)
        self.hover_rect_back.center = self.back_rect.center

    def hover_effect(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        if self.nxt_room_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, 'grey', self.hover_rect_next, 0, 2)
            if click: 
                return "next"

        if self.back_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, 'grey', self.hover_rect_back, 0, 2)

    def draw(self):
        self.screen.blit(self.room_number_text, self.room_number_rect)
        self.screen.blit(self.nxt_room_txt, self.nxt_room_rect)
        self.screen.blit(self.back_txt, self.back_rect)

    def update(self):
        room_variable = self.hover_effect()
        self.draw()

        return room_variable

class WhiteRoom(DefaultRoom):
    def __init__(self, screen, s_width, s_height) -> None:
        super().__init__(screen, s_width, s_height, "", True)

        self.nxt_room_txt = self.font.render("NEXT ROOM", True, 'black')
        self.nxt_room_rect = self.nxt_room_txt.get_rect()
        self.nxt_room_rect.center = (s_width / 2, s_height / 2)

        self.white_sheet = pygame.Surface((self.nxt_room_rect.width + 10, self.nxt_room_rect.height + 10))
        self.white_sheet.fill((255, 255, 255))
        self.white_sheet_rect = self.white_sheet.get_rect()
        self.white_sheet_rect.center = self.nxt_room_rect.center

        self.dragging = False

    def hover_effect(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.back_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, 'grey', self.back_rect.inflate(5, 5), 0, 2)

        if self.nxt_room_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, 'grey', self.nxt_room_rect, 0, 2)

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.back_txt, self.back_rect)
        self.screen.blit(self.nxt_room_txt, self.nxt_room_rect)
        self.screen.blit(self.white_sheet, self.white_sheet_rect)

    def update(self):
        self.drag()
        self.hover_effect()
        self.draw()

    def drag(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.dragging:
            self.white_sheet_rect.x = mouse_pos[0] - self.offset_x
            self.white_sheet_rect.y = mouse_pos[1] - self.offset_y

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.white_sheet_rect.collidepoint(event.pos):
                self.dragging = True
                self.offset_x = event.pos[0] - self.white_sheet_rect.x
                self.offset_y = event.pos[1] - self.white_sheet_rect.y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False



# ----------------------------------------------------------------------------------------------------------------------

# class WhiteRoom(DefaultRoom):
#     def __init__(self,screen, s_width, s_height) -> None:
#         super().__init__(screen, s_width, s_height, "", True)

#         self.width, self.height = 40,40
#         self.nxt_room_rect = pygame.Rect(0,0, self.width, self.height)
#         self.nxt_room_rect.center = (s_width/2, s_height/2)

#     def drag(self):

#     def draw(self):
#         pygame.draw.rect(self.screen, 'white', self.nxt_room_rect)
        
        
#     def update(self):
#         self.draw()


