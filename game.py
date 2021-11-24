import pygame, sys
from pygame.constants import SCRAP_SELECTION
from random import randint

def animate_floor(width):
    if width <= -576:
        width = 0
    width -= 1

    screen.blit(FLOOR_SURFACE, (width, 900))
    screen.blit(FLOOR_SURFACE, (width + 576, 900))

    return width

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/bluebird-midflap.png').convert()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(center = (100,512))
        self.movement = 0
        self.gravity = 0.25

    def update(self):
        self.movement += self.gravity
        self.rect.y += self.movement
        self.input()
    
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.movement = 0
            self.movement -= 10

class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.xpos = 1024
        self.speed = 3

        self.top_ypos = randint(-100,300)
        self.image  = pygame.image.load('assets/pipe-green.png').convert()
        self.image = pygame.transform.scale2x(self.image)
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect(center = (self.xpos, self.top_ypos))

    def update(self):
        super()
        self.rect.x -= self.speed
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


pygame.init()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()

# Game constants
BACKGROUND_DAY_SURFACE = pygame.image.load('assets/background-day.png').convert()
BACKGROUND_DAY_SURFACE = pygame.transform.scale2x(BACKGROUND_DAY_SURFACE)

FLOOR_SURFACE = pygame.image.load('assets/base.png').convert()
FLOOR_SURFACE = pygame.transform.scale2x(FLOOR_SURFACE)

# Game variables
floor_x_posistion = 0
gravity = 0.25
game_active = True

bird = pygame.sprite.GroupSingle()
bird.add(Bird())

pipes = pygame.sprite.Group()

PIPE_TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(PIPE_TIMER, 1500)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_SPACE:
                    bird_movement = 0
                    bird_movement -= 12
                case pygame.K_q:
                    pygame.quit()
                    sys.exit()

        if game_active:
            if event.type == PIPE_TIMER:
                pipes.add(Pipe())
    
    screen.blit(BACKGROUND_DAY_SURFACE, (0,0))
    floor_x_posistion = animate_floor(floor_x_posistion)
    
    bird.draw(screen)
    bird.update()

    pipes.draw(screen)
    pipes.update()

    pygame.display.update()
    clock.tick(120)
    