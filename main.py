# This file was created by: Eli Rose
#Assistace from Jude Hammers and ChatGPT
#Design Goals: Make a start and end screen that once you tap a key the game begins. 
# Design goal= pending, I cant figure out how to make both the start screen have text and have a game after the start screen.




#Game with working start screen but there is no game

# import pygame as pg
# import sys
# from settings import *
# from sprites import *
# from random import randint
# from os import path
# from time import sleep
# from math import floor

# class Game:
#     def __init__(self):
#         pg.init()
#         self.screen = pg.display.set_mode((WIDTH, HEIGHT))
#         pg.display.set_caption(TITLE)
#         self.clock = pg.time.Clock()
#         self.load_data()
#         self.start_time = pg.time.get_ticks()
#         self.time_limit = 45  # Countdown timer limit in seconds
#         self.running = True
#         self.show_start_screen()

#     def load_data(self):
#         game_folder = path.dirname(__file__)
#         self.map_data = []
#         with open(path.join(game_folder, 'map.txt'), 'rt') as f:
#             for line in f:
#                 print(line)
#                 self.map_data.append(line)

#     def new(self):
#         print("create new game...")
#         self.all_sprites = pg.sprite.Group()
#         self.walls = pg.sprite.Group()
#         self.coins = pg.sprite.Group()
#         self.mobs = pg.sprite.Group()  # Add a group for mobs
#         for row, tiles in enumerate(self.map_data):
#             print(row)
#             for col, tile in enumerate(tiles):
#                 print(col)
#                 if tile == '1':
#                     print("a wall at", row, col)
#                     Wall(self, col, row)
#                 if tile == 'P':
#                     self.player = Player(self, col, row)
#                 if tile == 'C':
#                     Coin(self, col, row)
#                 if tile == 'M':  # Create a mob where 'M' is found in the map
#                     Mob(self, col, row)

#     def run(self):
#         while self.running:
#             self.dt = self.clock.tick(FPS) / 1000
#             self.events()
#             self.update()
#             self.draw()
#             self.check_time()

#     def quit(self):
#         pg.quit()
#         sys.exit()

#     def update(self):
#         self.all_sprites.update()

#     def draw_grid(self):
#         for x in range(0, WIDTH, TILESIZE):
#             pg.draw.line(self.screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
#         for y in range(0, HEIGHT, TILESIZE):
#             pg.draw.line(self.screen, LIGHTGRAY, (0, y), (WIDTH, y))

#     def draw_text(self, surface, text, size, color, x, y):
#         font_name = pg.font.match_font('arial')
#         font = pg.font.Font(font_name, size)
#         text_surface = font.render(text, True, color)
#         text_rect = text_surface.get_rect()
#         text_rect.topleft = (x, y)
#         surface.blit(text_surface, text_rect)

#     def draw_clock(self, surface, time_left, color, x, y, radius):
#         font_name = pg.font.match_font('arial')
#         font = pg.font.Font(font_name, 24)
#         text_surface = font.render(f"Time: {time_left}", True, color)
#         text_rect = text_surface.get_rect()
#         text_rect.center = (x, y)
        
#         # Draw clock text
#         surface.blit(text_surface, text_rect)

#     def draw(self):
#         self.screen.fill(BGCOLOR)
#         self.draw_grid()
#         self.all_sprites.draw(self.screen)
#         self.draw_text(self.screen, str(self.player.moneybag), 64, WHITE, 1, 1)
#         # Displaying time
#         time_left = max(0, self.time_limit - (pg.time.get_ticks() - self.start_time) // 1000)
#         self.draw_clock(self.screen, time_left, BLUE, WIDTH // 2, 50, 30)
#         pg.display.flip()

#     def events(self):
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 self.quit()
#             elif event.type == pg.KEYUP:
#                 self.running = False  # Start the game when any key is pressed

#     def check_time(self):
#         # Reset the game if time runs out
#         if pg.time.get_ticks() - self.start_time >= self.time_limit * 1000:
#             print("Time's up! Resetting game...")
#             self.new()  # Restart the game
#             self.start_time = pg.time.get_ticks()  # Reset the timer

#     def show_start_screen(self):
#         self.screen.fill(BLACK)
#         self.draw_text(self.screen, "Press any key to begin", 30, WHITE, WIDTH//2, HEIGHT//2)
#         pg.display.flip()
#         self.wait_for_key()

#     def wait_for_key(self):
#         waiting = True
#         while waiting:
#             for event in pg.event.get():
#                 if event.type == pg.QUIT:
#                     self.quit()
#                 elif event.type == pg.KEYUP:
#                     waiting = False

# g = Game()
# g.run()













import pygame as pg
import sys
from settings import *
from sprites import *
from random import randint
from os import path
from time import sleep
from math import floor



class Game:  
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
        self.start_time = pg.time.get_ticks()
        self.time_limit = 20  # Countdown timer limit in seconds
        self.running = True
        # self.show_start_screen()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                print(line)
                self.map_data.append(line)

    def new(self):
        print("create new game...")
        self.load_data()
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.mobs = pg.sprite.Group()  # Add a group for mobs
        self.obstacles = pg.sprite.Group()
        self.loop_counter = 0
        for row, tiles in enumerate(self.map_data):
            self.loop_counter +=1
            print(self.loop_counter)
            # print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                    # print("a wall at", row, col)
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                # if tile == 'C':
                #     Coin(self, col, row)
                # # if tile == 'O':
                # #     Obstacle(self, col, row)
                # if tile == 'M':  # Create a mob where 'M' is found in the map
                #     Mob(self, col, row)

    def run(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
            self.check_time()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        # self.obstacles.update()
        

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGRAY, (0, y), (WIDTH, y))

    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_surface, text_rect)

    def draw_clock(self, surface, time_left, color, x, y, radius):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, 24)
        text_surface = font.render(f"Time: {time_left}", True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        
        # Draw clock text 
        surface.blit(text_surface, text_rect)

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen, str(self.player.moneybag), 64, WHITE, 1, 1)
        # Displaying time
        time_left = max(0, self.time_limit - (pg.time.get_ticks() - self.start_time) // 1000)
        self.draw_clock(self.screen, time_left, BLUE, WIDTH // 2, 50, 30)
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            elif event.type == pg.KEYUP:
                self.running = False 

    def check_time(self):
        # Reset the game if time runs out
        if pg.time.get_ticks() - self.start_time >= self.time_limit * 1000:
            self.screen.fill(BGCOLOR)
            self.draw_text(self.screen,"Time's up! Resetting game...", 48, BLUE, WIDTH/4.3, HEIGHT/2.2)
            pg.display.flip()
            self.wait_for_key()
            # print("Time's up! Resetting game...")
            
    

    def show_start_screen(self):
        self.screen.fill(BLACK)
        self.draw_text(self.screen, "Press any key to begin", 30, WHITE, WIDTH//2, HEIGHT//2)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                elif event.type == pg.KEYUP:
                    waiting = False


g = Game()

while True:
    g.new()
    g.run()





    # def show_start_screen(self):
    #      self.screen.fill(BGCOLOR)
    #      self.draw_text(self.screen, "Press any button to start game", 48, BLUE, WIDTH/4.3, HEIGHT/2.2)
    #      pg.display.flip()
    #      self.wait_for_key()
    # def update(self, screen):
    #     self.all_sprites.update()
    #     if pg.sprite.spritecollideany(self.player, self.mobs):
    #         self.screen.fill(BGCOLOR)
    #     self.draw_text(self.screen, "You lose. Game over bum.", 48, BLUE, WIDTH/4.3, HEIGHT/2.2)
    #     pg.display.flip()
    #     self.wait_for_key()
    #     running = False  # Or handle player death differently

 

 

    # def show_start_screen(self):
    #     self.screen.fill(BLUE)
    #     self.draw_text(self.screen, "Begin", 64, BLACK, WIDTH / 2, HEIGHT / 4)
    #     self.draw_text(self.screen, "Press any key to start", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)

    #     pg.display.flip()
    #     self.wait_for_key()

    # def show_end_screen(self):
    #     self.screen.fill(BLACK)
    #     self.draw_text(self.screen, "Game Over", 64, WHITE, WIDTH / 2, HEIGHT / 4)
    #     self.draw_text(self.screen, "You scored {self.player.moneybag} coins", 22, WHITE, WIDTH / 2, HEIGHT / 2)
    #     self.draw_text(self.screen, "Press any key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
    #     pg.display.flip()
    #     self.wait_for_key()
  

   #OG Base game

# import pygame as pg
# import sys
# from settings import *
# from sprites import *
# from random import randint
# from os import path
# from time import sleep
# from math import floor

# class Game:
#     def __init__(self):
#         pg.init()
#         self.screen = pg.display.set_mode((WIDTH, HEIGHT))
#         pg.display.set_caption(TITLE)
#         self.clock = pg.time.Clock()
#         self.load_data()
#         self.start_time = pg.time.get_ticks()
#         self.time_limit = 45  # Countdown timer limit in seconds

#     def load_data(self):
#         game_folder = path.dirname(__file__)
#         self.map_data = []
#         with open(path.join(game_folder, 'map.txt'), 'rt') as f:
#             for line in f:
#                 print(line)
#                 self.map_data.append(line)

#     def new(self):
#         print("create new game...")
#         self.all_sprites = pg.sprite.Group()
#         self.walls = pg.sprite.Group()
#         self.coins = pg.sprite.Group()
#         self.mobs = pg.sprite.Group()  # Add a group for mobs
#         for row, tiles in enumerate(self.map_data):
#             print(row)
#             for col, tile in enumerate(tiles):
#                 print(col)
#                 if tile == '1':
#                     print("a wall at", row, col)
#                     Wall(self, col, row)
#                 if tile == 'P':
#                     self.player = Player(self, col, row)
#                 if tile == 'C':
#                     Coin(self, col, row)
#                 if tile == 'M':  # Create a mob where 'M' is found in the map
#                     Mob(self, col, row)

#     def run(self):
#         while True:
#             self.dt = self.clock.tick(FPS) / 1000
#             self.events()
#             self.update()
#             self.draw()
#             self.check_time()

#     def quit(self):
#          pg.quit()
#          sys.exit()

#     def update(self):
#         self.all_sprites.update()

#     def draw_grid(self):
#         for x in range(0, WIDTH, TILESIZE):
#             pg.draw.line(self.screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
#         for y in range(0, HEIGHT, TILESIZE):
#             pg.draw.line(self.screen, LIGHTGRAY, (0, y), (WIDTH, y))

#     def draw_text(self, surface, text, size, color, x, y):
#         font_name = pg.font.match_font('arial')
#         font = pg.font.Font(font_name, size)
#         text_surface = font.render(text, True, color)
#         text_rect = text_surface.get_rect()
#         text_rect.topleft = (x*TILESIZE, y*TILESIZE)
#         surface.blit(text_surface, text_rect)

#     def draw_clock(self, surface, time_left, color, x, y, radius):
#         font_name = pg.font.match_font('arial')
#         font = pg.font.Font(font_name, 24)
#         text_surface = font.render(f"Time: {time_left}", True, color)
#         text_rect = text_surface.get_rect()
#         text_rect.center = (x, y)
        
#         # Draw clock text
#         surface.blit(text_surface, text_rect)

#     def draw(self):
#         self.screen.fill(BGCOLOR)
#         self.draw_grid()
#         self.all_sprites.draw(self.screen)
#         self.draw_text(self.screen, str(self.player.moneybag), 64, WHITE, 1, 1)
#         # Displaying time
#         time_left = max(0, self.time_limit - (pg.time.get_ticks() - self.start_time) // 1000)
#         self.draw_clock(self.screen, time_left, BLUE, WIDTH // 2, 50, 30)
#         pg.display.flip()

#     def show_start_screen(self):
#         self.screen.fill(BLACK)
#         self.draw_text(self.screen, "Press any key to begin", 30, WHITE, WIDTH//2, HEIGHT//2)
#         pg.display.flip()
#         self.wait_for_key()

#     def events(self):
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 self.quit()

#     def check_time(self):
#         # Reset the game if time runs out
#         if pg.time.get_ticks() - self.start_time >= self.time_limit * 1000:
#             print("Time's up! Resetting game...")
#             self.new()  # Restart the game
#             self.start_time = pg.time.get_ticks()  # Reset the timer

    


# g = Game()

# while True:
#     g.new()
#     g.run()





