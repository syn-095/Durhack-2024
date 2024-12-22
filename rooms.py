try:
    import pygame, time, random
    import keypad
except Exception as e:
    print ('one or more modules not available')

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

        self.nxt_room_txt = self.font.render("NEXT ROOM", True, 'black')
        # self.nxt_room_rect = self.nxt_room_txt.get_rect()
        # self.nxt_room_rect.midbottom = (s_width/2, self.s_h/2)  

        # self.hover_rect = pygame.Rect(0,0,self.nxt_room_rect.width + 5, self.nxt_room_rect.height + 5)
        # self.hover_rect.center = self.nxt_room_rect.center

        # ROOM 1 TEXT --------------
        self.room1_txt = self.font.render("ROOM 1", True, 'black')
        self.room1_rect = self.room1_txt.get_rect()
        self.room1_rect.midbottom = (s_width/2, self.s_h/2 - 20) 

        self.room1_hover_rect = pygame.Rect(0,0,self.room1_rect.width + 5, self.room1_rect.height + 5)
        self.room1_hover_rect.center = self.room1_rect.center
        # -------

        # ROOM 1 BIS ------------------
        self.room1bis_txt = self.font.render("ROOM 1(bis)", True, 'black')
        self.room1bis_rect = self.room1bis_txt.get_rect()
        self.room1bis_rect.midtop = (s_width/2, self.s_h/2 + 20)

        self.room1bis_hover_rect = pygame.Rect(0,0,self.room1bis_rect.width + 5, self.room1bis_rect.height + 5)
        self.room1bis_hover_rect.center = self.room1bis_rect.center
        # ---------

    def hover_effect(self, room_unlocked):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        if self.nxt_room_rect.collidepoint(mouse_pos) and not room_unlocked:
            pygame.draw.rect(self.screen, 'grey', self.hover_rect_next, 0, 2)
            if click: 
                return "next"
            

        if self.room1_rect.collidepoint(mouse_pos) and room_unlocked:
            pygame.draw.rect(self.screen, 'grey', self.room1_hover_rect, 0, 2)
            if click: 
                return "room 1"
            
        if self.room1bis_rect.collidepoint(mouse_pos) and room_unlocked:
            pygame.draw.rect(self.screen, 'grey', self.room1bis_hover_rect, 0, 2)
            if click: 
                return "room 1 bis"

    def draw(self, room_unlocked):
        self.screen.blit(self.room_number_text, self.room_number_rect)
        if not room_unlocked: self.screen.blit(self.nxt_room_txt, self.nxt_room_rect)
        else: 
            self.screen.blit(self.room1_txt, self.room1_rect)
            self.screen.blit(self.room1bis_txt, self.room1bis_rect)

    def update(self, room_unlocked):
        exit=self.hover_effect(room_unlocked)
        self.draw(room_unlocked)

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
            if click: return "back"

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

        self.keypad = keypad.Keypad((self.s_w/2 - 50, self.s_h*2/3 + 20), 100, 100, self.screen)

        self.periodic_img = pygame.image.load("Images/periodic_table.jpg")
        self.periodic_img = pygame.transform.scale(self.periodic_img, (600, 300))
        self.periodic_rect = self.periodic_img.get_rect(midbottom=(self.s_w/2, self.elements_rects[0][1].top))

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

        self.screen.blit(self.periodic_img, self.periodic_rect)
        self.screen.blit(self.room_number_text, self.room_number_rect)
        self.screen.blit(self.back_txt, self.back_rect)
        self.screen.blit(self.lock_img, self.lock_rect)

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
        self.crowbar_img = pygame.transform.scale(self.crowbar_img, (30, 30))
        self.crowbar_rect = self.crowbar_img.get_rect(center = (self.s_w/2, self.s_h*2/3))

        self.crowbar_picked = False

    def hover(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        if self.crowbar_rect.collidepoint(mouse):
            if pygame.mouse.get_pressed()[0]:
                self.crowbar_picked = True
                return "crowbar picked"

        if self.window_rect.collidepoint(mouse):
            if pygame.mouse.get_pressed()[0] and self.crowbar_picked:
                return "next"
            
        if self.back_rect.collidepoint(mouse):
            pygame.draw.rect(self.screen, 'grey', self.back_rect_hover)
            if click: return 'back'

    def draw(self):
        self.screen.blit(self.window_img, self.window_rect)
        self.screen.blit(self.back_txt, self.back_rect)
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

class Room1bis(DefaultRoom):
    def __init__(self, screen, s_width, s_height, difference_to_entrance, difference_to_elements_room, no_room_display=True, no_room_back=False, no_next_room=False):
        super().__init__(screen, s_width, s_height, no_room_display, no_room_back, no_next_room)

        # LIGHT FUNCTIONS
        # N -> changes states of all letters except itself
        # E -> changes state of itself + neighbours
        # X -> if N is lit, changes state of even letters, odd if not
        # T -> permutes state of E and R 
        # R -> changes state of a completely random letter
        # O -> if NEXT is all lit up, lights up all of ROOM, if not turns off all of NEXT
        # O -> if more than 1 letter is yet to be lit, lights up first unlit letter from left, if not unlights every letter
        # M -> lights/unlights itself

        self.dif_to_entrance = difference_to_entrance
        self.dif_to_elements = difference_to_elements_room

        self.letters = ['N','E','X','T','','R','O','O','M']
        self.letter_rects = []

        for index, letter in enumerate(self.letters):
            letter_txt = self.font.render(letter, True, 'grey')
            letter_rect = letter_txt.get_rect(center = (self.s_w/3 + 70*index, self.s_h/2))
            lit = False
            timeout = False
            self.letter_rects.append([letter_txt, letter_rect, lit, timeout])

        self.all_lit = False

        hover_rect_w = self.letter_rects[8][1].right - self.letter_rects[0][1].left
        self.hover_rect_next = pygame.Rect(self.letter_rects[0][1].left - 5, self.letter_rects[8][1].top - 5, hover_rect_w + 10, self.letter_rects[0][1].height + 10)

    def interactions(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        if self.back_rect.collidepoint(mouse):
            pygame.draw.rect(self.screen, 'grey', self.back_rect_hover)
            if click: return ['back', self.dif_to_entrance]

        def check_all_lit_letters():
            lit_letters = []
            for index, rect in enumerate(self.letter_rects):
                if rect[2] and index != 4: lit_letters.append(rect[1])
            
            if len(lit_letters) == len(self.letter_rects) - 1:
                self.all_lit = True
                return True
            else: 
                self.all_lit = False
                return False


        # LIGHTING UP LETTERS
        if not check_all_lit_letters():
            for index, rect in enumerate(self.letter_rects):
                if rect[1].collidepoint(mouse):

                    if index == 0 and click and not rect[3]:
                        for i, l in enumerate(self.letter_rects):
                            if i != 0:
                                l[2] = not l[2]
                                colour = 'yellow' if l[2] else 'grey'
                                l[0] = self.font.render(self.letters[i], True, colour)

                        rect[3] = True

                    elif index == 1 and click and not rect[3]:
                        self.letter_rects[index-1][2] = not self.letter_rects[index-1][2]
                        colour = 'yellow' if self.letter_rects[index-1][2] else 'grey'
                        self.letter_rects[index-1][0] = self.font.render(self.letters[index - 1], True, colour)

                        self.letter_rects[index][2] = not self.letter_rects[index][2]
                        colour = 'yellow' if self.letter_rects[index][2] else 'grey'
                        self.letter_rects[index][0] = self.font.render(self.letters[index], True, colour)

                        self.letter_rects[index+1][2] = not self.letter_rects[index+1][2]
                        colour = 'yellow' if self.letter_rects[index+1][2] else 'grey'
                        self.letter_rects[index+1][0] = self.font.render(self.letters[index+1], True, colour)

                        rect[3] = True

                    elif index == 2 and click and not rect[3]:
                        if self.letter_rects[0][2]:
                            for i, l in enumerate(self.letter_rects):
                                if i%2 == 0:
                                    l[2] = not l[2]
                                    colour = 'yellow' if l[2] else 'grey'
                                    l[0] = self.font.render(self.letters[i], True, colour)
                        else:
                            for i, l in enumerate(self.letter_rects):
                                if i%2 != 0:
                                    l[2] = not l[2]
                                    colour = 'yellow' if l[2] else 'grey'
                                    l[0] = self.font.render(self.letters[i], True, colour)

                        rect[3] = True
                    
                    elif index == 3 and click and not rect[3]:

                        e_state = self.letter_rects[1][2]
                        r_state = self.letter_rects[5][2]
                        
                        self.letter_rects[1][2] = r_state
                        colour = 'yellow' if r_state else 'grey'
                        self.letter_rects[1][0] = self.font.render(self.letters[1], True, colour)

                        self.letter_rects[5][2] = e_state
                        colour = 'yellow' if e_state else 'grey'
                        self.letter_rects[5][0] = self.font.render(self.letters[5], True, colour)

                        rect[3] = True
                    
                    elif index == 5 and click and not rect[3]:
                        letter_index = random.randint(0,len(self.letters) - 2)
                        if letter_index >= 4: letter_index += 1

                        self.letter_rects[letter_index][2] = not self.letter_rects[letter_index][2]
                        colour = 'yellow' if self.letter_rects[letter_index][2] else 'grey'
                        self.letter_rects[letter_index][0] = self.font.render(self.letters[letter_index], True, colour)

                        rect[3] = True

                    elif index == 6 and click and not rect[3]:
                        if self.letter_rects[0][2] and self.letter_rects[1][2] and self.letter_rects[2][2] and self.letter_rects[3][2]:
                            for i, l in enumerate(self.letter_rects):
                                if i > 4: 
                                    l[2] = True
                                    l[0] = self.font.render(self.letters[i], True, 'yellow')
                        
                        else:
                            for i, l in enumerate(self.letter_rects):
                                if i < 4: 
                                    l[2] = False
                                    l[0] = self.font.render(self.letters[i], True, 'grey')
                        
                        rect[3] = True

                    elif index == 7 and click and not rect[3]:
                        unlit_letters = []
                        for i, l in enumerate(self.letter_rects):
                            if not l[2] and i != 4: unlit_letters.append(i)
                        
                        print (len(unlit_letters))

                        if len(unlit_letters) >= 2:
                            self.letter_rects[unlit_letters[0]][2] = True
                            self.letter_rects[unlit_letters[0]][0] = self.font.render(self.letters[unlit_letters[0]], True, 'yellow')
                        else:
                            for i, l in enumerate(self.letter_rects):
                                l[2] = False
                                l[0] = self.font.render(self.letters[i], True, 'grey')  

                        rect[3] = True

                    elif index == 8:
                        if click and rect[2] and not rect[3]: 
                            rect[0] = self.font.render(self.letters[index], True, 'grey')  
                            rect[2] = False
                            rect[3] = True
                        elif click and not rect[2] and not rect[3]:
                            rect[0] = self.font.render(self.letters[index], True, 'yellow')
                            rect[2] = True
                            rect[3] = True

                    elif not click:
                        rect[3] = False 
        # ----
        elif self.all_lit:
            no_clicks = True
            for i, l in enumerate(self.letter_rects):
                if l[3]: no_clicks = False
            
            if self.hover_rect_next.collidepoint(mouse) and click and no_clicks:
                return ['next', self.dif_to_elements]
            
            for i, l in enumerate(self.letter_rects):
                l[3] = False
        # Checking if all letters are lit up & toggling button accordingly


    def draw(self):
        self.screen.blit(self.back_txt, self.back_rect)

        if self.all_lit:
            pygame.draw.rect(self.screen, 'grey', self.hover_rect_next)

        for rect in self.letter_rects:
            self.screen.blit(rect[0], rect[1])


    def update(self):
        room_variable = self.interactions()

        self.draw()

        return room_variable


if __name__ == '__main__':
    print ('please run main file to play the game')