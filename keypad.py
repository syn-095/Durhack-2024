import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display variables
WIDTH = 400
HEIGHT = 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Pad")

# Font setup
font = pygame.font.SysFont('Arial', 30)

# Number pad layout
numbers = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

# Function to draw the number pad
def draw_number_pad():
    screen.fill(WHITE)
    
    # Draw rectangles for numbers
    rect_width = WIDTH // 3
    rect_height = HEIGHT // 4
    
    for row in range(3):
        for col in range(3):
            pygame.draw.rect(screen, GRAY, (col * rect_width, row * rect_height + HEIGHT // 4, rect_width, rect_height))
    
    # Draw numbers
    for i, row in enumerate(numbers):
        for j, num in enumerate(row):
            text = font.render(num, True, BLACK)
            screen.blit(text, (j * rect_width + 10, (i + 1) * rect_height + HEIGHT // 10))

# Function to draw entered numbers
def draw_entered_numbers(numbers):
    text = font.render('Entered: ' + ''.join(numbers), True, BLACK)
    screen.blit(text, (10, 30))

# Main game loop
entered_numbers = []
correct_combination = '1234'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            
            # Check if clicked on a number
            rect_width = WIDTH // 3
            rect_height = HEIGHT // 4
            
            for row in range(3):
                for col in range(3):
                    if (col * rect_width <= mouse_x < (col + 1) * rect_width and
                        (row * rect_height + HEIGHT // 4 <= mouse_y < (row + 1) * rect_height + HEIGHT // 4)):
                        entered_numbers.append(numbers[row][col])
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if entered_numbers:
                    entered_numbers.pop()
            elif event.key == pygame.K_RETURN:
                if ''.join(entered_numbers) == correct_combination:
                    print("Correct combination!")
                else:
                    print("Incorrect combination.")
                entered_numbers = []
            elif event.unicode.isdigit():
                entered_numbers.append(event.unicode)

    draw_number_pad()
    draw_entered_numbers(entered_numbers)
    pygame.display.flip()

    # Limit frame rate to 60 FPS
    pygame.time.Clock().tick(60)