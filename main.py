import pygame, sys, time
from pygame.math import Vector2
from rooms import rooms

class Game:
    def __init__(self) -> None:
        self.entrance = rooms.Entrance(screen, W, H)
        self.room_1 = rooms.Room1(screen, W, H)
        self.white_room = rooms.WhiteRoom(screen, W, H)
        self.elements_room = rooms.ElementsRoom(screen, W, H, "002")
        self.key_room = rooms.KeyRoom(screen, W, H)
        self.window_room = rooms.WindowRoom(screen, W, H, "100")
        self.window_end = rooms.Window_end(screen, W, H)

        self.white_room_num = 3
        self.elements_room_num = 4
        self.key_room_num = 5
        self.window_room_num = 6
        self.window_end_num = self.window_room_num + 1

        self.current_room = 1

    def update(self):
        room_variable = None
        sleep_time = 0.2

        if self.current_room == 1:
            room_variable = self.entrance.update()
            if room_variable: time.sleep(sleep_time)

        elif self.current_room == 2: 
            room_variable = self.room_1.update()
            if room_variable: time.sleep(sleep_time)

        elif self.current_room == self.white_room_num:
            room_variable = self.white_room.update()
            if room_variable: time.sleep(sleep_time)

        elif self.current_room == self.elements_room_num:
            room_variable = self.elements_room.update()
            if room_variable: time.sleep(sleep_time)

        elif self.current_room == self.key_room_num:
            room_variable = self.key_room.update()
            if room_variable: time.sleep(sleep_time)

        elif self.current_room == self.window_room_num:
            room_variable = self.window_room.update()
            if room_variable: time.sleep(sleep_time)

        elif self.current_room == self.window_end_num:
            room_variable = self.window_end.update()
            if room_variable: time.sleep(sleep_time)

        if room_variable == "back":  self.current_room -= 1
        if room_variable == "next": self.current_room += 1



pygame.init()

screen_info = pygame.display.Info()

W, H = screen_info.current_w - 20, screen_info.current_h - 100

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # => fullscreen window
# screen = pygame.display.set_mode((W,H))

game = Game()

while True:
    for event in pygame.event.get():
        # QUITTING OPTIONS:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        # ----------------------------
        if game.current_room == game.white_room_num:
            game.white_room.handle_events(event)
        if game.current_room == game.elements_room_num:
            game.elements_room.handle_events(event)
        if game.current_room == game.key_room_num:
            game.key_room.handle_events(event)
        
    screen.fill('white')

    game.update()

    pygame.display.update()
