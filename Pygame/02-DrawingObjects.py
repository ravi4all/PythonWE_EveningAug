import pygame

pygame.init()

black = 0,0,0
white = 255,255,255
red = 255,0,0
color_1 = 105,180,200

screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Game Demo")

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit() # quit pygame
            quit() # quit python

    screen.fill(color_1)
    pygame.draw.rect(screen,red,[0,0,50,50])
    pygame.draw.circle(screen,red,[100,100],50)

    pygame.display.update()

