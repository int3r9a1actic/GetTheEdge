# ============= #
#     RDUTC     #
#  #GetTheEdge  #
#               #
# Jason B White #
#               #
# 06 April 2021 #
# ============= #

#-- Import necessary modules ---------------------------------------#
import pygame
import random
import sys

#-- Set up pygame --------------------------------------------------#
from pygame.locals import *
pygame.init()
WIDTH = 800
HEIGHT = 800
SCREENSIZE = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("#GetTheEdge at Ron Dearing UTC")

#-- Define the "Keep Off" Pad class --------------------------------#
class Pad(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH//4*3, HEIGHT//4*3))
        self.image.fill((239, 111, 254))
        self.x = random.randint(WIDTH//3, WIDTH//3*2)
        self.y = random.randint(HEIGHT//3, HEIGHT//3*2)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        pass

#-- Define a block class for the "Avoid the Blocks" ----------------#
class Block(pygame.sprite.Sprite):

    speedx = random.randint(-1, 1)
    speedy = random.randint(-1, 1)

    def __init__(self, in_x, in_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH//10, HEIGHT//10))
        self.image.fill((255, 0, 0))
        self.x = in_x
        self.y = in_y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
    def update(self):
        self.rect.move_ip(Block.speedx//2, Block.speedy//2)

#-- Define a Reward class for sponsors rewards --------------------#
class Reward(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH//10, HEIGHT//10))
        self.image.fill((0, 0, 255))
        self.x = WIDTH//4
        self.y = HEIGHT//4
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.speed = 1

    def update(self):
        pass

#-- Define the Player class ----------------------------------------#
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH//10, HEIGHT//10))
        self.image.fill((51, 51, 153))
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.speed = 10

    def update(self, in_keys):
        self.rect.move_ip((in_keys[K_LEFT] * -self.speed) + (in_keys[K_RIGHT] * self.speed), (in_keys[K_UP] * -self.speed) + (in_keys[K_DOWN] * self.speed))
        # -- Keep player on the screen ---------#
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

#-- Create the game object -----------------------------------------#
class Game():
    def __init__(self):
        #-- 
        self.background = pygame.Surface(SCREEN.get_size())
        self.background.fill((128, 128, 255))
        self.clock = pygame.time.Clock()
        self.start()
    
    def start(self):
        #- Start -------------------------------#
        #self.menu()
        self.score = self.play()
        #self.gameover(self.score)

    def menu(self):
        #-- Display the menu -------------------#
        pass

    def play(self):
        print("Play")
        #-- Play the game ----------------------#
        self.pad = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.rewards = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.pad.add(Pad())
        for i in range(-500, 1300, 200):
            for j in range(-500, 1300, 200):
                self.blocks.add(Block(i, j))

        self.rewards.add(Reward())
        self.player.add(Player())
        self.score = 0
        while True:
            #-- Check for events ---------------#
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
            
            keys = pygame.key.get_pressed()

            #-- Update the sprites -------------#
            self.pad.update()
            self.blocks.update()
            self.rewards.update()
            self.player.update(keys)

            #-- Draw the screen ----------------#
            SCREEN.blit(self.background, (0, 0))
            self.pad.draw(SCREEN)
            self.blocks.draw(SCREEN)
            self.rewards.draw(SCREEN)
            self.player.draw(SCREEN)

            #-- Update the screen --------------#
            pygame.display.flip()

            #-- Limit the framerate
            self.clock.tick(60)
        return self.score

#-- Start the game -------------------------------------------------#
game = Game()