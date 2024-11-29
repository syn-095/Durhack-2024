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
            ['CE', '0', 'B']  # CE: Clear, C: backspace
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
                key_list = [key for key in self.pressed_keys]
                key_list = key_list[0:-1]
                self.pressed_keys = ""
                for key in key_list: self.pressed_keys += key
            if key[pygame.K_DELETE]:
                self.pressed_keys = ""

        if pygame.mouse.get_pressed()[0]:
            for key, rect in self.key_rects:
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        if key == 'CE':
                            self.pressed_keys = ""
                        if key == 'B':
                            key_list = [key for key in self.pressed_keys]
                            key_list = key_list[0:-1]
                            self.pressed_keys = ""
                            for key in key_list: self.pressed_keys += key
                        else:
                            self.pressed_keys += key
                        time.sleep(sleep_time)
                        
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

