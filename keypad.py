import pygame, sys, time

class Keypad:
    def __init__(self, position, width, height, screen):
        self.position = position
        self.width = width
        self.height = height
        self.screen = screen
        self.keys = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['C', '0', 'E']  # C: Clear, E: Enter
        ]
        self.font = pygame.font.SysFont("Arial", 30)
        self.pressed_keys = ""
        self.create_keypad()

    def create_keypad(self):
        self.key_rects = []
        key_width = self.width // 3
        key_height = self.height // 4
        for row_idx, row in enumerate(self.keys):
            for col_idx, key in enumerate(row):
                rect = pygame.Rect(
                    self.position[0] + col_idx * key_width,
                    self.position[1] + row_idx * key_height,
                    key_width, key_height
                )
                self.key_rects.append((key, rect))

    def draw(self):
        pressed_text_surf = self.font.render(self.pressed_keys, True, 'black')
        pressed_text_rect = pressed_text_surf.get_rect(center = (self.position[0] + self.width // 2, self.position[1] - 30))
        self.screen.blit(pressed_text_surf, pressed_text_rect)

        for key, rect in self.key_rects:
            pygame.draw.rect(self.screen, 'grey', rect)
            text_surf = self.font.render(key, True, 'black')
            text_rect = text_surf.get_rect(center=rect.center)
            self.screen.blit(text_surf, text_rect)

    def handle_event(self):
        key = pygame.key.get_pressed()
        sleep_time = 0.3
        if True: # MAKING TOGGLE FOR READABILITY
            if key[pygame.K_1]:
                self.pressed_keys += "1"
                time.sleep(sleep_time)
            if key[pygame.K_2]:
                self.pressed_keys += "2"
                time.sleep(sleep_time)
            if key[pygame.K_3]:
                self.pressed_keys += "3"
                time.sleep(sleep_time)
            if key[pygame.K_4]:
                self.pressed_keys += "4"
                time.sleep(sleep_time)
            if key[pygame.K_5]:
                self.pressed_keys += "5"
                time.sleep(sleep_time)
            if key[pygame.K_6]:
                self.pressed_keys += "6"
                time.sleep(sleep_time)
            if key[pygame.K_7]:
                self.pressed_keys += "7"
                time.sleep(sleep_time)
            if key[pygame.K_8]:
                self.pressed_keys += "8"
                time.sleep(sleep_time)
            if key[pygame.K_9]:
                self.pressed_keys += "9"
                time.sleep(sleep_time)
            if key[pygame.K_0]:
                self.pressed_keys += "0"
                time.sleep(sleep_time)
            
            if key[pygame.K_BACKSPACE]:
                self.pressed_keys = self.pressed_keys[:-1]

        if pygame.mouse.get_pressed()[0]:
            for key, rect in self.key_rects:
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        if key == 'C':
                            self.pressed_keys = ""
                        elif key == 'E':
                            return self.pressed_keys
                        else:
                            self.pressed_keys += key
                            time.sleep(0.3)
                        
        return self.pressed_keys


import pygame

if __name__ == '__main__':
    # Initialize pygame and create a display
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # Create an instance of the Keypad
    keypad = Keypad(position=(300, 200), width=200, height=250, screen=screen)

    # Game loop for testing purposes
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
              # Print the pressed keys when Enter is pressed

        screen.fill((240, 240, 240))  # Background color

        result = keypad.handle_event()
        if result is not None:
            print(f"Pressed keys: {result}")

        keypad.draw()
        pygame.display.flip()

    pygame.quit()


# class NumberPad:
#     def __init__(self, parent_surface, x, y, width, height, entered_Nos, correct_code):
#         self.parent_surface = parent_surface
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.correct_code = correct_code
#         self.entered_numbers = entered_Nos
#         self.numbers = [
#             ['1', '2', '3'],
#             ['4', '5', '6'],
#             ['7', '8', '9']
#         ]
#         self.clock = pygame.time.Clock()

#     def draw(self):
#         screen = pygame.display.get_surface()
#         rect = pygame.Rect(self.x, self.y, self.width, self.height)
#         pygame.draw.rect(screen, (200, 200, 200), rect)
        
#         rect_width = self.width // 3
#         rect_height = self.height // 4
        
#         for row in range(3):
#             for col in range(3):
#                 pygame.draw.rect(screen, (100, 100, 100), 
#                                  (col * rect_width + self.x, row * rect_height + self.y + self.height // 4, 
#                                   rect_width, rect_height))
        
#         for i, row in enumerate(self.numbers):
#             for j, num in enumerate(row):
#                 text = pygame.font.SysFont('Arial', 30).render(num, True, (0, 0, 0))
#                 screen.blit(text, (j * rect_width + self.x + 10, 
#                                    (i + 1) * rect_height + self.y + self.height // 10))

#     def handle_events(self, event):
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_x, mouse_y = event.pos
            
#             rect_width = self.width // 3
#             rect_height = self.height // 4
            
#             for row in range(3):
#                 for col in range(3):
#                     if (col * rect_width + self.x <= mouse_x < (col + 1) * rect_width + self.x and
#                         (row * rect_height + self.y + rect_height <= mouse_y < 
#                          (row + 1) * rect_height + self.y + rect_height)):
#                         self.entered_numbers.append(self.numbers[row][col])
        
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_BACKSPACE:
#                 if self.entered_numbers:
#                     self.entered_numbers.pop()
#             elif event.key == pygame.K_RETURN:
#                 if ''.join(self.entered_numbers) == self.correct_code:
#                     print("Correct combination!")
#                 else:
#                     print("Incorrect combination.")
#                 self.entered_numbers = []
#                 global entered_nums
#                 entered_nums.clear()

#             elif event.unicode.isdigit():
#                 self.entered_numbers.append(event.unicode)
#                 entered_nums = self.entered_numbers

#     def update(self):
#         self.draw()
#         for event in pygame.event.get():
#             self.handle_events(event)
#         # screen = pygame.display.get_surface()
#         # text = pygame.font.SysFont('Arial', 30).render(f'Entered: {"".join(self.entered_numbers)}', True, (0, 0, 0))
#         # screen.blit(text, (self.x + 10, self.y + self.height // 10))


# #----------------------------------- Example usage-----------------------------------------------------------------------------------
# def create_window(width, height):
#     pygame.init()
#     screen = pygame.display.set_mode((width, height))
#     clock = pygame.time.Clock()

#     running = True
#     global entered_nums
#     entered_nums = []
#     while running:

#         screen.fill((255, 255, 255))
        
#         # Create and draw number pad on the right half of the screen with code 1234
#         number_pad = NumberPad(screen, width // 2, 0, width // 2, height, entered_nums, '1234')
#         number_pad.update()


#         for event in pygame.event.get():
#             number_pad.handle_events(event)
#             if event.type == pygame.QUIT:
#                 running = False
           
            
        

#         pygame.display.flip()
#         clock.tick(60)

#     pygame.quit()
#     sys.exit()

# if __name__ == "__main__":
#     create_window(800, 600)