import pygame

pygame.init()

black = 0,0,0
white = 255,255,255
red = 255,0,0
color_1 = 105,180,200

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Game Demo")

x = 0
y = 0
moveX = 1
moveY = 1

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit() # quit pygame
            quit() # quit python

    screen.fill(color_1)
    # pygame.draw.rect(screen,red,[x,y,50,50])
    pygame.draw.circle(screen, red, [x, y], 50)

    x += moveX
    y += moveY

    if x > width - 50:
        moveX = -1
    elif x < 50:
        moveX = 1

    if y > height - 50:
        moveY = -1
    elif y < 50:
        moveY = 1

    pygame.display.update()