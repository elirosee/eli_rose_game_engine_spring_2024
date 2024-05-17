# This file was created by: Eli Rose
# ASsistance from chatGpt and friends 
 
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
        self.level = 1
        self.start_time = pg.time.get_ticks()
        self.time_limit = 60  # Countdown timer limit in seconds
        self.running = True
        self.show_start_screen()
        self.map_file = 'map.txt' #show map one at beginning 
        self.load_data

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, self.map_file), 'rt') as f:
            for line in f:
                self.map_data.append(line.strip())
    
    def load_level(self,level):
        self.level = level
        self.load_data()

    def new(self):
        print("create new game...")
        self.load_data()
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.mobs = pg.sprite.Group()  # Add a group for mobs
        self.obstacles = pg.sprite.Group()
        self.portal = pg.sprite.Group()
        self.loop_counter = 0
        

        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                    print("a wall at", row, col)
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'O':
                    Obstacle(self, col, row)
                if tile == 'M':  # Create a mob where 'M' is found in the map
                    Mob(self, col, row)
                if tile == 'T': #Portal
                    Portal(self, col, row)

    def run(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
            # self.check_time()

    def quit(self):
        pg.quit()
        sys.exit()

#if Obstacle or Mob collide with player game ends
    def update(self):
        self.all_sprites.update()
        self.obstacles.update()
        if pg.sprite.spritecollideany(self.player, self.obstacles):
            self.restart_game()
        self.mobs.update()
        if pg.sprite.spritecollideany(self.player, self.mobs):
            self.restart_game()
        if pg.sprite.spritecollideany (self.player, self.portal): #If player runs into portal open map 2
            self.next_level()
            self.map_file = 'map2.txt'
            self.load_data()
            self.new()
            self.run()
            
            

        
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

    def show_end_screen(self):
        self.screen.fill(BLACK)
        self.draw_text(self.screen, "You lost!", 30, WHITE, WIDTH//2, HEIGHT//2)
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
    
    #Load the next level
    def next_level(self):
        print("Loading next level...")
        self.load_level('map2.txt')
        
    

g = Game()

while True:
    g.new()
    g.run()




