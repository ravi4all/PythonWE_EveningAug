import pygame

pygame.init()

black = 0,0,0
white = 255,255,255
color_1 = 105,180,200

width = 600
height = 512

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Race")

image_1 = pygame.image.load("images/road.png")
image_2 = pygame.image.load("images/road.png")
car_1 = pygame.image.load("images/car_2.png")

backgroundY1 = 0
backgroundY2 = -height
moveY = 0

clock = pygame.time.Clock()
FPS = 80

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit pygame
            quit() # quit python

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moveY = 8

        elif event.type == pygame.KEYUP:
            moveY = 0

    backgroundY1 += moveY
    backgroundY2 += moveY

    screen.blit(image_1, (0,backgroundY1))
    screen.blit(image_2, (0,backgroundY2))
    screen.blit(car_1, (180,height - 220))

    if backgroundY1 > height:
        backgroundY1 = -height
    elif backgroundY2 > height:
        backgroundY2 = -height

    pygame.display.update()
    clock.tick(FPS)

