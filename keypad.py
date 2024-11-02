import pygame
import sys

class NumberPad:
    def __init__(self, parent_surface, x, y, width, height, entered_Nos, correct_code):
        self.parent_surface = parent_surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.correct_code = correct_code
        self.entered_numbers = entered_Nos
        self.numbers = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
        self.clock = pygame.time.Clock()

    def draw(self):
        screen = pygame.display.get_surface()
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (200, 200, 200), rect)
        
        rect_width = self.width // 3
        rect_height = self.height // 4
        
        for row in range(3):
            for col in range(3):
                pygame.draw.rect(screen, (100, 100, 100), 
                                 (col * rect_width + self.x, row * rect_height + self.y + self.height // 4, 
                                  rect_width, rect_height))
        
        for i, row in enumerate(self.numbers):
            for j, num in enumerate(row):
                text = pygame.font.SysFont('Arial', 30).render(num, True, (0, 0, 0))
                screen.blit(text, (j * rect_width + self.x + 10, 
                                   (i + 1) * rect_height + self.y + self.height // 10))

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            
            rect_width = self.width // 3
            rect_height = self.height // 4
            
            for row in range(3):
                for col in range(3):
                    if (col * rect_width + self.x <= mouse_x < (col + 1) * rect_width + self.x and
                        (row * rect_height + self.y + rect_height <= mouse_y < 
                         (row + 1) * rect_height + self.y + rect_height)):
                        self.entered_numbers.append(self.numbers[row][col])
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if self.entered_numbers:
                    self.entered_numbers.pop()
            elif event.key == pygame.K_RETURN:
                if ''.join(self.entered_numbers) == self.correct_code:
                    print("Correct combination!")
                else:
                    print("Incorrect combination.")
                self.entered_numbers = []
                global entered_nums
                entered_nums.clear()

            elif event.unicode.isdigit():
                self.entered_numbers.append(event.unicode)
                entered_nums = self.entered_numbers

    def update(self):
        self.draw()
        for event in pygame.event.get():
            self.handle_events(event)
        screen = pygame.display.get_surface()
        text = pygame.font.SysFont('Arial', 30).render(f'Entered: {"".join(self.entered_numbers)}', True, (0, 0, 0))
        screen.blit(text, (self.x + 10, self.y + self.height // 10))


#----------------------------------- Example usage-----------------------------------------------------------------------------------
def create_window(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    running = True
    global entered_nums
    entered_nums = []
    while running:

        screen.fill((255, 255, 255))
        
        # Create and draw number pad on the right half of the screen with code 1234
        number_pad = NumberPad(screen, width // 2, 0, width // 2, height, entered_nums, '1234')
        number_pad.update()


        for event in pygame.event.get():
            number_pad.handle_events(event)
            if event.type == pygame.QUIT:
                running = False
           
            
        



        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

create_window(800, 600)