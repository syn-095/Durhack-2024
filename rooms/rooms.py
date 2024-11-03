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

        self.elements = ["Be", "N", "Li", "Ni", "He"]

        self.elements_rects = []
        for index, element in enumerate(self.elements):
            text = self.font.render(f"{element}", True, 'black')
            rect = text.get_rect(center=(self.s_w/2 - 200 + index*100, self.s_h/2))
            self.elements_rects.append([text, rect, [self.s_w/2 - 200 + index*100, self.s_h/2]])

        self.lock_img = pygame.image.load("Images/Lock.png")
        self.lock_img = pygame.transform.scale(self.lock_img, (50, 50))
        self.lock_rect = self.lock_img.get_rect(center=(self.s_w/2, self.s_h/2 + 75))

        self.keypad = keypad.Keypad((self.s_w/2 - 45, self.s_h*2/3 + 20), 100, 100, self.screen)

        self.periodic_img = pygame.image.load("Images/periodic_table.jpg")
        self.periodic_img = pygame.transform.scale(self.periodic_img, (500, 250))
        self.periodic_rect = self.periodic_img.get_rect(center=(self.s_w/2, self.s_h/2 - 175))

        self.door_img = pygame.image.load("Images/door.png")
        self.door_img = pygame.transform.scale(self.door_img, (150, 300))
        self.door_rect = self.door_img.get_rect(center = (self.s_w/5, self.s_h/2))

        self.barricade_img = pygame.image.load("Images/Door_barricade.png")
        self.barricade_img = pygame.transform.scale(self.barricade_img, (150, 300))
        self.barricade_rect = self.door_img.get_rect(center = (self.s_w/5, self.s_h/2))

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
        self.screen.blit(self.periodic_img, self.periodic_rect)

        self.screen.blit(self.door_img, self.door_rect)
        self.screen.blit(self.barricade_img, self.barricade_rect)

        for element in self.elements_rects:
            self.screen.blit(element[0], element[1])

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

class KeyRoom(DefaultRoom):
    def __init__(self, screen, s_width, s_height, no_room_display=True, no_room_back=True, no_next_room=True):
        super().__init__(screen, s_width, s_height, "", no_room_display, no_room_back, no_next_room)
        
        self.left_door_open = False

        if True: # CREATING ALL IMAGES VARIABLES
            self.broken_key_img = pygame.image.load("Images/Keys/Key_Broken.png")
            self.broken_key_img = pygame.transform.scale(self.broken_key_img, (150, 150))
            self.broken_key_rect = self.broken_key_img.get_rect(midbottom=(self.s_w / 2, self.s_h - 40))

            self.fixed_key_img = pygame.image.load("Images/Keys/Key_Fixed.png")
            self.fixed_key_img = pygame.transform.scale(self.fixed_key_img, (150, 150))
            self.fixed_key_rect = self.fixed_key_img.get_rect(midtop=(self.s_w / 2, 40))

            # RIGHT DOOR
            self.right_door_img = pygame.image.load("Images/door.png")
            self.right_door_img = pygame.transform.scale(self.right_door_img, (200, 350))
            self.right_door_rect = self.right_door_img.get_rect(center=(self.s_w * 3 / 4, self.s_h / 2))

            self.right_door_lock_img = pygame.image.load("Images/lock.png")
            self.right_door_lock_img = pygame.transform.scale(self.right_door_lock_img, (25, 25))
            self.right_door_lock = self.right_door_lock_img.get_rect(midleft=(self.right_door_rect.left, self.right_door_rect.centery))

            # LEFT DOOR
            self.left_door_img = pygame.image.load("Images/door.png")
            self.left_door_img = pygame.transform.scale(self.left_door_img, (200, 350))
            self.left_door_rect = self.left_door_img.get_rect(center=(self.s_w/4, self.s_h / 2))

            self.left_door_lock_img = pygame.image.load("Images/lock.png")
            self.left_door_lock_img = pygame.transform.scale(self.left_door_lock_img, (25,25))
            self.left_door_lock = self.left_door_lock_img.get_rect(midleft=(self.left_door_rect.left, self.left_door_rect.centery))

 
            self.create_key_txt = self.font.render("create key", True, "black")
            self.create_key_rect = self.create_key_txt.get_rect(center = (self.s_w/2, self.s_h/2 + 120))
            self.create_key_hover = pygame.Rect(0,0,self.create_key_rect.width + 5, self.create_key_rect.height + 5)
            self.create_key_hover.center = self.create_key_rect.center 

            self.boxes = [self.create_box((self.s_w / 2 - 150, self.s_h / 2)),
                        self.create_box((self.s_w / 2, self.s_h / 2)),
                        self.create_box((self.s_w / 2 + 150, self.s_h / 2))]

            self.current_images = [0, 0, 0]  # indexes for the current images being displayed
            self.images = [
                [pygame.transform.scale(pygame.image.load(f"Images/Keys/set1/P{i + 1}.png"), (200, 200)) for i in range(4)],
                [pygame.transform.scale(pygame.image.load(f"Images/Keys/set2/P{i + 1}.png"), (200, 200)) for i in range(4)],
                [pygame.transform.scale(pygame.image.load(f"Images/Keys/set3/P{i + 1}.png"), (200, 200)) for i in range(4)]
            ]

    def create_box(self, center_pos):
        box = pygame.Surface((100, 100))  # Adjusted to fit arrows and images
        box.fill('white')
        box_rect = box.get_rect(center=center_pos)

        up_arrow = pygame.image.load("Images/arrows/arrow_smaller_up.png")
        up_arrow = pygame.transform.scale(up_arrow, (40, 35))
        up_arrow_rect = up_arrow.get_rect(midbottom=(box_rect.midtop))

        down_arrow = pygame.image.load("Images/arrows/arrow_smaller.png")
        down_arrow = pygame.transform.scale(down_arrow, (40, 35))
        down_arrow_rect = down_arrow.get_rect(midtop=(box_rect.midbottom))

        return {
            'box': box,
            'rect': box_rect,
            'up_arrow': up_arrow,
            'up_rect': up_arrow_rect,
            'down_arrow': down_arrow,
            'down_rect': down_arrow_rect
        }

    def hover_effect(self):
        def check_key_combination():
            if self.current_images == [0,3,1]: 
                self.left_door_open = True
                self.left_door_img = pygame.image.load("Images/Open_door.png")
                self.left_door_img = pygame.transform.scale(self.left_door_img, (200, 360))

        click = pygame.mouse.get_pressed()[0]
        if self.create_key_hover.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, 'grey', self.create_key_hover, 0, 2)
            if click and check_key_combination(): self.left_door_open = True
        
        if self.left_door_rect.collidepoint(pygame.mouse.get_pos()) and self.left_door_open:
            if click: return "next"

    def draw(self):
        if self.left_door_open: self.screen.blit(self.fixed_key_img, self.fixed_key_rect)
        self.screen.blit(self.broken_key_img, self.broken_key_rect)

        self.screen.blit(self.right_door_img, self.right_door_rect)
        self.screen.blit(self.right_door_lock_img, self.right_door_lock)

        self.screen.blit(self.left_door_img, self.left_door_rect)
        if not self.left_door_open:
            self.screen.blit(self.left_door_lock_img, self.left_door_lock)

        self.screen.blit(self.create_key_txt, self.create_key_rect)

        for i, box in enumerate(self.boxes):
            self.screen.blit(box['box'], box['rect'])
            
            image = self.images[i][self.current_images[i]]
            image_rect = image.get_rect(center=box['rect'].center)
            self.screen.blit(image, image_rect)

            # self.screen.blit(box['up_arrow'], box['up_rect'])
            # self.screen.blit(box['down_arrow'], box['down_rect'])

            self.screen.blit(box['up_arrow'], box['up_rect'])
            self.screen.blit(box['down_arrow'], box['down_rect'])


    def update(self):
        room_variable = self.hover_effect()
        self.draw()

        return room_variable

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, box in enumerate(self.boxes):

                if box['up_rect'].collidepoint(event.pos):
                    self.current_images[i] = (self.current_images[i] + 1) % len(self.images[i])
                elif box['down_rect'].collidepoint(event.pos):
                    self.current_images[i] = (self.current_images[i] - 1) % len(self.images[i])

class WindowRoom(DefaultRoom):
    def __init__(self, screen, s_width, s_height, room_name: str, no_room_display=False, no_room_back=False, no_next_room=False):
        super().__init__(screen, s_width, s_height, room_name, no_room_display, no_room_back, no_next_room)

        self.window_img = pygame.image.load("Images/Window.png")
        self.window_img = pygame.transform.scale(self.window_img, (300, 300))
        self.window_rect = self.window_img.get_rect(center = (self.s_w/2, self.s_h/2 - 200))

        self.crowbar_img = pygame.image.load("Images/Crowbar.png")
        self.crowbar_img = pygame.transform.scale(self.crowbar_img, (300, 300))
        self.crowbar_rect = self.crowbar_img.get_rect(midbottom = (self.s_w/2, self.s_h))

        self.crowbar_picked = False

    def hover(self):
        if self.crowbar_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.crowbar_picked = True

        if self.window_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.crowbar_picked:
                return "next"

    def draw(self):
        print ('displaying window')
        self.screen.blit(self.window_img, self.window_rect)
        if not self.crowbar_picked: self.screen.blit(self.crowbar_img, self.crowbar_rect)


    def update(self):
        room_variable = self.hover()
        self.draw()

        return room_variable

class Window_end(DefaultRoom):
    def __init__(self, screen, s_width, s_height,  no_room_display=True, no_room_back=True, no_next_room=True):
        super().__init__(screen, s_width, s_height, "", no_room_display, no_room_back, no_next_room)

        self.end_txt = self.font.render("YOU HAVE ESCAPED!", True, 'black')
        self.end_rect = self.end_txt.get_rect(center = (self.s_w/2, self.s_h/2))

    def draw(self):
        self.screen.blit(self.end_txt, self.end_rect)

    def update(self):
        self.draw()

