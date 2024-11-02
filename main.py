import pygame, sys
from pygame.math import Vector2
from rooms import room_1

class Game:
    def __init__(self) -> None:
        self.room_1 = room_1.Room1(screen, W, H)
        self.room_2 = room_1.Room2(screen, W, H)
        self.current_room = 1

    def update(self):
        exit = False
        if self.current_room == 1:
            exit = self.room_1.update()
        elif self.current_room == 2: 
            exit = self.room_2.update()
        
        if exit: self.current_room += 1


pygame.init()

screen_info = pygame.display.Info()

W, H = screen_info.current_w - 20, screen_info.current_h - 100

# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) => fullscreen window
screen = pygame.display.set_mode((W,H))

game = Game()

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

    game.update()

    pygame.display.update()
