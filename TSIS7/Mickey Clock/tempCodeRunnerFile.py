pygame.init()

clock = pygame.time.Clock()

HEIGHT = 960
WIDTH = 1280

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
pygame.display.set_caption('Clock')