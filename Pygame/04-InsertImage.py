import pygame

pygame.init()

black = 0,0,0
white = 255,255,255
red = 255,0,0
color_1 = 105,180,200

width = 1000
height = 600

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Game Demo")

ball = pygame.image.load("ball_2.png")
bg = pygame.image.load("game_bg.jpg")

x = 0
y = 0
moveX = 10
moveY = 10

clock = pygame.time.Clock()
FPS = 80

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit() # quit pygame
            quit() # quit python

    # screen.fill(color_1)
    screen.blit(bg, (0,0))
    screen.blit(ball, (x,y))

    x += moveX
    y += moveY

    if x > width - 150:
        moveX = -10
    elif x < 0:
        moveX = 10

    if y > height - 155:
        moveY = -10
    elif y < 0:
        moveY = 10

    pygame.display.update()
    clock.tick(FPS)