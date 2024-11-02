import pygame, sys
from pygame.math import Vector2

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
