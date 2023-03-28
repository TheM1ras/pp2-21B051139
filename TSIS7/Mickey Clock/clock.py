import pygame
from datetime import datetime

def rot_center(image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

pygame.init()

clock = pygame.time.Clock()

HEIGHT = 960
WIDTH = 1280

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
pygame.display.set_caption('Clock')

clock_body = pygame.image.load("clock_without_arms.jpg")


minute_hand = pygame.image.load("Minute.png")
minute_hand = pygame.transform.scale(minute_hand, (450, 450))

second_hand = pygame.image.load("Seconds.png")
second_hand = pygame.transform.scale(second_hand, (450, 450))

running = True

while running:
    screen.blit(clock_body, (0, 0))
    
    time = datetime.now()

    min = time.minute
    sec = time.second

    rects = second_hand.get_rect(center=(WIDTH//2, HEIGHT//2)) 
    surfs, rs = rot_center(second_hand, rects, 360-sec*6)
    screen.blit(surfs, rs)

    rectm = minute_hand.get_rect(center=(WIDTH//2, HEIGHT//2)) 
    surfm, rm = rot_center(minute_hand, rectm, 360-min*6)
    screen.blit(surfm, rm)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
    

    clock.tick(20)
    pygame.display.flip()
pygame.quit()