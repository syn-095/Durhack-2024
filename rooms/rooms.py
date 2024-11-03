import pygame, time
import keypad

class DefaultRoom: # Parent class for rooms
    def __init__(self, screen, s_width, s_height, room_name : str, no_room_display = False, no_room_back = False, no_next_room = False):
        
        self.screen = screen
        self.s_w, self.s_h = s_width, s_height

        # setting a font for 
        self.font = pygame.font.SysFont("Monospace", 50)

        if not no_room_display:
            self.room_number_text = self.font.render(f"{room_name}", True, 'black')
            self.room_number_rect = self.room_number_text.get_rect()
            self.room_number_rect.midtop = (s_width/2, 15)

        if not no_room_back:
            self.back_txt = self.font.render("BACK", True, 'black')
            self.back_rect = self.back_txt.get_rect()
            self.back_rect.midbottom = (s_width/2, s_height - 60)

            self.back_rect_hover = pygame.Rect(0,0,self.back_rect.width + 5, self.back_rect.height + 5)
            self.back_rect_hover.center = self.back_rect.center

        if not no_next_room:
            self.nxt_room_txt = self.font.render("NEXT ROOM", True, 'black')
            self.nxt_room_rect = self.nxt_room_txt.get_rect()
            self.nxt_room_rect.center = (s_width / 2, s_height / 2)

            self.hover_rect_next = pygame.Rect(0, 0, self.nxt_room_rect.width + 5, self.nxt_room_rect.height + 5)
            self.hover_rect_next.center = self.nxt_room_rect.center

class Entrance(DefaultRoom):
    def __init__(self, screen, s_width, s_height) -> None:
        super().__init__(screen, s_width, s_height, "ENTRANCE")

        # self.nxt_room_txt = self.font.render("NEXT ROOM", True, 'black')
        # self.nxt_room_rect = self.nxt_room_txt.get_rect()
        # self.nxt_room_rect.midbottom = (s_width/2, self.s_h/2)  

        # self.hover_rect = pygame.Rect(0,0,self.nxt_room_rect.width + 5, self.nxt_room_rect.height + 5)
        # self.hover_rect.center = self.nxt_room_rect.center

    def hover_effect(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        if self.nxt_room_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, 'grey', self.hover_rect_next, 0, 2)
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

        self.white_sheet = pygame.Surface((self.nxt_room_rect.width + 10, self.nxt_room_rect.height + 10))
        self.white_sheet.fill((255, 255, 255))
        self.white_sheet_rect = self.white_sheet.get_rect()
        self.white_sheet_rect.center = self.nxt_room_rect.center

        self.dragging = False

    def hover_effect(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        def check_nxt_discovered():
            if self.dragging or (self.white_sheet_rect.right >= self.nxt_room_rect.right and self.white_sheet_rect.left <= self.nxt_room_rect.left and self.white_sheet_rect.bottom >= self.nxt_room_rect.bottom and self.white_sheet_rect.top <= self.nxt_room_rect.top): 
                print ("no click")
                return False
            else: return True

        if self.back_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, 'grey', self.back_rect_hover, 0, 2)
            if click: return "back"

        if self.nxt_room_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, 'grey', self.hover_rect_next, 0, 2)
            if click and check_nxt_discovered(): return "next"

        if self.back_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, 'grey', self.back_rect_hover, 0, 2)

        if self.nxt_room_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, 'grey', self.hover_rect_next, 0, 2)

    def draw(self):
        self.screen.blit(self.back_txt, self.back_rect)
        self.screen.blit(self.nxt_room_txt, self.nxt_room_rect)
        self.screen.blit(self.white_sheet, self.white_sheet_rect)

    def update(self):
        self.drag()
        room_variable = self.hover_effect()
        self.draw()

        return room_variable

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

class ElementsRoom(DefaultRoom):
    def __init__(self, screen, s_width, s_height, room_name):
        super().__init__(screen, s_width, s_height, room_name=room_name, no_next_room=True)

        self.elements = ["Re", "N", "Li", "Ni", "He"]

        self.elements_rects = []
        for index, element in enumerate(self.elements):
            text = self.font.render(f"{element}", True, 'black')
            rect = text.get_rect(center=(self.s_w/2 - 200 + index*100, self.s_h/2))
            self.elements_rects.append([text, rect, [self.s_w/2 - 200 + index*100, self.s_h/2]])

        self.lock_img = pygame.image.load("Images/Lock.png")
        self.lock_img = pygame.transform.scale(self.lock_img, (50, 50))
        self.lock_rect = self.lock_img.get_rect(center=(self.s_w/2, self.s_h/2 + 75))

        self.keypad = keypad.Keypad((self.s_w/2 - 45, self.s_h*2/3 + 20), 100, 100, self.screen)

        self.clicked_lock = False
        self.dragging = False
        self.dragged_element = None

    def hover_effect(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        if self.back_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, 'grey', self.back_rect.inflate(5, 5), 0, 2)
            if click:
                return "back"

        if self.lock_rect.collidepoint(mouse_pos) and click:
            self.clicked_lock = True
            time.sleep(0.1)

    def draw(self):
        if self.clicked_lock:
            self.keypad.draw()

        for element in self.elements_rects:
            self.screen.blit(element[0], element[1])

        self.screen.blit(self.room_number_text, self.room_number_rect)
        self.screen.blit(self.back_txt, self.back_rect)
        self.screen.blit(self.lock_img, self.lock_rect)

    def update(self):
        room_variation = self.hover_effect()
        self.draw()

        result = self.keypad.handle_event()
        if result == "342872":
            return 'next'

        return room_variation

    def drag(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.dragging and self.dragged_element is not None:
            self.dragged_element[1].center = mouse_pos

    def handle_events(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for element in self.elements_rects:
                    if element[1].collidepoint(event.pos):
                        self.dragging = True
                        self.dragged_element = element
                        self.offset_x = event.pos[0] - element[1].x
                        self.offset_y = event.pos[1] - element[1].y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False
                if self.dragged_element is not None:
                    for element in self.elements_rects:
                        if element != self.dragged_element and element[1].collidepoint(mouse_pos):
                            # Swap positions
                            self.dragged_element[1].center, element[1].center = element[1].center, self.dragged_element[1].center
                    self.dragged_element = None

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging and self.dragged_element is not None:
                self.drag()

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


