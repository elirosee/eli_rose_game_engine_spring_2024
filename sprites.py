# This file was created by Eli Rose

#Works cited: Assistance from AI

import pygame as pg
from pygame.sprite import Sprite
from settings import *
import os 
 
 #Tells game to use the character folder to access the ghost
game_folder = os.path.dirname (__file__)
img_folder = os.path.join(game_folder, 'characters')

#creating player class
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        # init super class
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.moneybag = 0
 
    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED  
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED  
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED  
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
 
    # def move(self, dx=0, dy=0):
    #     if not self.collide_with_walls(dx, dy):
    #         self.x += dx
    #         self.y += dy
 
    # def collide_with_walls(self, dx=0, dy=0):
    #     for wall in self.game.walls:
    #         if wall.x == self.x + dx and wall.y == self.y + dy:
    #             return True
    #     return False
 
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
 
    def collide_with_group(self, group, kill):
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            if str(hits[0].__class__.__name__) == "Coin":
                self.moneybag += 1
 
    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        #add collision later
        self.collide_with_walls('x')
        self.rect.y = self.y
        # add collision later
        self.collide_with_walls('y')
        # self.collide_with_group(self.game.coins, True)
        # coin_hits = pg.sprite.spritecollide(self.game.coins, True)
        # if coin_hits:
        #     print("I got a coin")

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.groups = game.all_sprites, game.obstacles
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.speed = 5
        self.direction = 1  

    def update(self):
        self.rect.y += self.speed * self.direction
        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            self.direction *= -1
 
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
 
class Coin(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.coins
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder, 'ghost smaller.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.vx, self.vy = 0, 0

    def update(self):
        self.vx, self.vy = 0, 0  # Reset velocities
        self.calculate_velocity()
        self.rect.x += self.vx * self.game.dt
    #     self.check_collision('x')
        self.rect.y += self.vy * self.game.dt
    #     self.check_collision('y')

# # Mob Speed
    def calculate_velocity(self):
        dx = self.game.player.rect.centerx - self.rect.centerx
        dy = self.game.player.rect.centery - self.rect.centery
        dist = max(100, abs(dx) + abs(dy))
        self.vx = 100 * dx / dist
        self.vy = 100 * dy / dist

    def check_collision(self, direction):
        if direction == 'x':
            self.rect.x += self.vx * self.game.dt
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
#Make ghost go through wall
            for wall in hits:
                if self.vx > 0:
                    self.rect.right = wall.rect.left
                    self.vx *= -1  
                if self.vx < 0:
                    self.rect.left = wall.rect.right
                    self.vx *= -1  
                self.rect.x = int(self.rect.x)
        if direction == 'y':
            self.rect.y += self.vy * self.game.dt
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            for wall in hits:
                if self.vy > 0:
                    self.rect.bottom = wall.rect.top
                    self.vy *= -1
                elif self.vy < 0:
                    self.rect.top = wall.rect.bottom
                    self.vy *= -1  
                self.rect.y = int(self.rect.y)

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.groups = game.all_sprites, game.obstacles
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.speed = 2
        self.direction = 1  

    def update(self):
        self.rect.y += self.speed * self.direction
        if self.rect.bottom > HEIGHT or self.rect.top < 0:

            self.direction *= -1

class Portal(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.portal
        pg. sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(MAGENTA)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self. rect.y = y * TILESIZE



    # def check_collisions(self):
    #     if pg.sprite.spritecollideany(self, self.game.portal):
    #         self.game.nect_level()
