import pygame
import sys

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

HEIGHT = 960
WIDTH = 1280

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

_songs = ["kevin-macleod_-_heartwarming.mp3", 
            "Taron Egerton - I'm Still Standing.mp3",
            "Neon Trees - Moving In The Dark.mp3"]


screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(white)
pygame.display.set_caption('Music Player')
font = pygame.font.Font('freesansbold.ttf', 32)
pygame.mixer.music.load(_songs[0])
pygame.mixer.music.play()
text = font.render(_songs[0], True, blue, white)
textRect = text.get_rect() 
textRect.center = (WIDTH // 2, HEIGHT // 2)

n = int(len(_songs))

pygame.mixer.music.load(_songs[0])
pygame.mixer.music.play()
text = font.render(_songs[0], True, blue, white)

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

def play_prev_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]
    _songs = _songs[1:] + [_songs[0]]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

screen.blit(text, (0, 0))

running = True

while running:
    screen.blit(screen, (0, 0))

    for event in pygame.event.get():
        if event.type == SONG_END:
            play_next_song()
        
        if event.type == pygame.QUIT:  
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                play_next_song()
                text = font.render(_songs[0], True, blue, white)
                screen.blit(text, (0, 0))
            elif event.key == pygame.K_LEFT:
                play_prev_song()
                text = font.render(_songs[0], True, blue, white)
                screen.blit(text, (0, 0))
            elif event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                elif not pygame.mixer.music.get_busy(): 
                    pygame.mixer.music.unpause()

    clock.tick(60)
    pygame.display.flip()
pygame.quit()