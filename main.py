import pygame, sys, time
from pygame.math import Vector2
import rooms

class Game:
    def __init__(self) -> None:
        self.entrance_num = 0
        self.room_1_num = 1
        self.room_1bis_num = 1.5
        self.white_room_num = 2
        self.elements_room_num = 3
        self.key_room_num = 4
        self.window_room_num = 5
        self.window_end_num = self.window_room_num + 1

        self.white_room_entered = False

        self.current_room = 0


        self.entrance = rooms.Entrance(screen, W, H)
        self.room_1 = rooms.Room1(screen, W, H)
        self.room_1bis = rooms.Room1bis(screen, W, H, self.room_1bis_num - self.entrance_num, self.elements_room_num-self.room_1bis_num)
        self.white_room = rooms.WhiteRoom(screen, W, H)
        self.elements_room = rooms.ElementsRoom(screen, W, H, "002")
        self.key_room = rooms.KeyRoom(screen, W, H)
        self.window_room = rooms.WindowRoom(screen, W, H, "100")
        self.window_end = rooms.Window_end(screen, W, H)

        self.inventory = []
        self.inv_crowbar_img = pygame.image.load('Images/Crowbar.png')
        self.inv_crowbar_img = pygame.transform.scale(self.inv_crowbar_img, (100, 100))
        self.inv_crowbar_rect = self.inv_crowbar_img.get_rect(bottomright = (W - 20, H - 20))

    def update(self):
        room_variable = None
        sleep_time = 0.3

        if self.current_room == self.entrance_num:
            room_variable = self.entrance.update(self.white_room_entered)
            if room_variable: time.sleep(sleep_time)

        elif self.current_room == self.room_1_num: 
            room_variable = self.room_1.update()
            if room_variable: time.sleep(sleep_time)

        elif self.current_room == self.room_1bis_num:
            room_variable = self.room_1bis.update()
            if room_variable: time.sleep(sleep_time)

        elif self.current_room == self.white_room_num:
            self.white_room_entered = True
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

        if len(self.inventory) != 0: 
            if 'crowbar' in self.inventory:
                pygame.draw.rect(screen, 'grey', self.inv_crowbar_rect, 0, 5)
                pygame.draw.rect(screen, 'black', self.inv_crowbar_rect, 1, 5)
                screen.blit(self.inv_crowbar_img, self.inv_crowbar_rect)

        # for every room (except 1 bis)
        if room_variable == "back": self.current_room -= 1
        if room_variable == "next": self.current_room += 1

        # for room 1 bis
        if type(room_variable) == list:
            if room_variable[0] == 'back': self.current_room -= room_variable[1]
            if room_variable[0] == 'next': self.current_room += room_variable[1]

        if room_variable == "room 1": self.current_room = self.room_1_num
        if room_variable == "room 1 bis": self.current_room = self.room_1bis_num

        if room_variable == "crowbar picked": self.inventory.append('crowbar')



pygame.init()

screen_info = pygame.display.Info()

W, H = screen_info.current_w - 20, screen_info.current_h - 120

# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #=> fullscreen window
screen = pygame.display.set_mode((W,H))

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
