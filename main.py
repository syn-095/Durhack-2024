import pygame, sys
from pygame.math import Vector2
from rooms import room_1

class Main:
    def __init__(self) -> None:
        room_width, room_height = 100, 75

        self.room_1 = room_1.Room1(room_width, room_height)




pygame.init()

screen_info = pygame.display.Info()

W, H = screen_info.current_w - 20, screen_info.current_h - 50

# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) => fulscreen window
screen = pygame.display.set_mode((W,H))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    screen.fill('white')

    pygame.display.update()
