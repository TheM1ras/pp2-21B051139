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
N = 0
p = 1
I = random.randint(1, 10)


#Screating texts and setting fonds
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
enemy_speed = font.render("Enemy speed up", True, RED)
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
        self.i = random.randint(1, 10)
        self.rect.center=(random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        global SPEED
        self.rect.move_ip(0, SPEED)
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
                self.rect.move_ip(0, -7)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,7)
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-7, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(7, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        global N
        global I
        if I >= 1 and I<= 5:
            super().__init__()
            self.image = pygame.image.load('coin.png')
            self.rect = self.image.get_rect()
            N = 1
        elif I >=6 and I<=8:
            super().__init__()
            self.image = pygame.image.load('3coin.png')
            self.image = pygame.transform.scale(self.image, (54, 54))
            self.rect = self.image.get_rect()
            N = 3
        elif I >=9 and I<=10:
            super().__init__()
            self.image = pygame.image.load('5coin.png')
            self.image = pygame.transform.scale(self.image, (54, 54))
            self.rect = self.image.get_rect()
            N = 5
        
        
                    
            
    def move(self):
        self.rect.move_ip(0, 0)
        if (self.rect.bottom > 600):
            self.rect.top = 30
            self.rect.center = (random.randint(130, 370), random.randint(130, 570))

    def update(self):
        global I
        if self.rect.colliderect(Player.rect):
            Player.coins += N
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
#pygame.time.set_timer(INC_SPEED, 15000)

while True:
    for event in pygame.event.get():
        '''
        if event.type == INC_SPEED:
            SPEED += 2
        '''
            
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #show score
    screen.blit(background, (0,0))
    scores = font_small.render(f"Score:{str(SCORE)}", True, BLACK)
    screen.blit(scores, (10,10))

    #moving our objects
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    #increasing speed of enemies every 25 coins
    if COINS >= 25*p:
        SPEED += 1
        p+=1
    
    #show enemy speed
    score = font_small.render(f"Speed:{SPEED}", True, BLACK)    
    screen.blit(score, (10, SCREEN_HEIGHT-30))

    #in this part we increase coins if player collide with coin and generate new coin after that
    if pygame.sprite.spritecollideany(p1, coins):
        I = random.randint(1, 10)
        c1.__init__()
        COINS = COINS + N
        c1.rect.center = (random.randint(30, 370), random.randint(130, 570))
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
