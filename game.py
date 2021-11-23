import pygame, sys
from pygame.constants import SCRAP_SELECTION

# Game constants
BACKGROUND_DAY_SURFACE = pygame.image.load('assets/background-day.png').convert()
BACKGROUND_DAY_SURFACE = pygame.transform.scale2x(BACKGROUND_DAY_SURFACE)
FLOOR_SURFACE = pygame.image.load('assets/base.png').convert()
FLOOR_SURFACE = pygame.transform.scale2x(FLOOR_SURFACE)

pygame.init()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()

# Game variables
floor_x_posistion = 0

def animate_floor(width):
    if width <= -576:
        width = 0
    width -= 1

    screen.blit(FLOOR_SURFACE, (width, 900))
    screen.blit(FLOOR_SURFACE, (width + 576, 900))

    return width

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(BACKGROUND_DAY_SURFACE, (0,0))
    floor_x_posistion = animate_floor(floor_x_posistion)
    

    pygame.display.update()
    clock.tick(60)
    