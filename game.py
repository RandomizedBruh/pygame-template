
import pygame


WIDTH = 800   
HEIGHT = 800

FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Моя перва игра кхехе")

clock = pygame.time.Clock()

isRunning = True

while isRunning:


    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

pygame.quit



