import sys
import pygame
import random, time
from pygame.locals import * 

pygame.init()

FPS = 30
framepersec = pygame.time.Clock()

#colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

#Screating texts and setting fonds
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load("Street.png")

screen = pygame.display.set_mode((400, 600))
screen.fill(WHITE)
pygame.display.set_caption("Racer")

background = pygame.image.load('Street.png')

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > 600):
            SCORE +=1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coin.png')
        self.rect = self.image.get_rect()
            
    def move(self):
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0) 

    def update(self):
        if self.rect.colliderect(Player.rect):
            Player.coins += 1
            self.kill()               

p1 = Player()
e1 = Enemy()
c1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(e1)
coins = pygame.sprite.Group()
coins.add(c1)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)
all_sprites.add(c1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 2
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()       

    screen.blit(background, (0,0))
    scores = font_small.render(f"Score:{str(SCORE)}", True, BLACK)
    screen.blit(scores, (10,10))

    #moving our objects
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    #in this part we increase score if player collide with coin and generate new coin after that
    if pygame.sprite.spritecollideany(p1, coins):
        COINS += 1
        c1.rect.center = (random.randint(30, 370), 0)
        pygame.display.update()

    #this part of code show in the screen the score of the player    
    score = font_small.render(f"Coins:{COINS}", True, BLACK)    
    screen.blit(score, ( SCREEN_WIDTH-100, 10))

    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()        

    pygame.display.update() 
    framepersec.tick(FPS)